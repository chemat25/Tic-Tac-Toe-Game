import math
import random


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
    
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            if square.isdigit():
                val = int(square)
                if val in range(9) and val in game.available_moves():
                    valid_square = True
                else:
                    print('Invalid square! Please enter a number that is available.')
            else:
                print('Invalid input! Please enter a number.')
    
        return val


class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # Choose random move for first move
            square = random.choice(game.available_moves())  
        else:
            #calling the alpha beta pruning function with alpha value as negative infinity and beta value as infinity
            square = self.alpha_beta(game, self.letter, -math.inf, math.inf)['position']
        return square

    def alpha_beta(self, game, player, alpha, beta):
        max_player = self.letter
        other_player = 'O'
        if player == 'X':
            other_player = 'O'
        else:
            other_player = 'X'

        if game.current_winner == other_player:
            if other_player == max_player:
                score = 1 * (game.num_empty_squares() + 1)
            else:
                score = -1 * (game.num_empty_squares() + 1)
            return {'position': None, 'score': score}
        elif not game.empty_squares():
            return {'position': None, 'score': 0}


        if player == max_player:
            best = {'position': None, 'score': -math.inf}
            possible_moves = game.available_moves()
            i = 0
            while i < len(possible_moves):
                possible_move = possible_moves[i]
                game.make_move(possible_move, player)
                sim_score = self.alpha_beta(game, other_player, alpha, beta)
                game.board[possible_move] = ' '
                game.current_winner = None
                sim_score['position'] = possible_move
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, best['score'])
                if alpha >= beta:
                    break
                i += 1

            return best
        else:
            best = {'position': None, 'score': math.inf}
            possible_moves = game.available_moves()
            i = 0
            while i < len(possible_moves):
                possible_move = possible_moves[i]
                game.make_move(possible_move, player)
                sim_score = self.alpha_beta(game, other_player, alpha, beta)
                game.board[possible_move] = ' '
                game.current_winner = None
                sim_score['position'] = possible_move
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])
                if alpha >= beta:
                    break
                i += 1
            return best
