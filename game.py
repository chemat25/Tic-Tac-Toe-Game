import math
import time
from player import HumanPlayer, AIPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.build_board()
        self.current_winner = None

    @staticmethod
    def build_board():
        #return [' ' for _ in range(9)]
        empty_board = []
        for i in range (9):
            empty_board.append(' ')
        return empty_board    
    

    def print_board(self):
        for i in range(3):
            row = self.board[i * 3: (i + 1) * 3]
            formatted_row = '| ' + ' | '.join(row) + ' |'
            print(formatted_row)


    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
    
        for row in number_board:
            formatted_row = '| ' + ' | '.join(row) + ' |'
            print(formatted_row)


    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # check the row
        row_index = math.floor(square / 3)
        row_start = row_index*3
        row_end = (row_index+1) * 3
        row = self.board[row_start:row_end]
        if all([s == letter for s in row]):
            return True
        # check the column
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        if square % 2 == 0:
            #check the principle diagonal
            diagonal1 = []
            for i in [0, 4, 8]:
                diagonal1.append(self.board[i])

            all_match = True
            for s in diagonal1:
                if s != letter:
                    all_match = False
                    break

            if all_match:
                return True

            #check the other diagonal
            diagonal2 = []
            for i in [2, 4, 6]:
                diagonal2.append(self.board[i])

            all_match1 = True
            for s in diagonal2:
                if s != letter:
                    all_match1 = False
                    break

            if all_match1:
                return True
        return False

    def empty_squares(self):
        if(' ' in self.board):
            return True
        else:
            return False


    def num_empty_squares(self):
        count = 0
        for i in range(9):
            if ' ' in self.board[i]:
                count+=1
        return count

    def available_moves(self):
        empty_indices = []
        for index, value in enumerate(self.board):
            if value == " ":
                empty_indices.append(index)
        return empty_indices

#It's time to play the game
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    current_player = 'X'    #Change the starting player here
    
    while game.empty_squares():
        if current_player == 'O':
            square = o_player.get_move(game)
        elif current_player == 'X':
            square = x_player.get_move(game)
        
        if game.make_move(square, current_player):
            if print_game:
                print(current_player + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(current_player + ' wins!')
                return current_player  # Exits the game
            #Player switch
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'
        
        time.sleep(0.8)
    
    if print_game:
        print("It's a tie!")
if __name__ == '__main__':
    x_player = AIPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)