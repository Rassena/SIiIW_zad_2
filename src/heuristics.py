# Control the center of the board
# Control the edges of the board
# Control the corners of the board
# Mobility
# Corner mobility
# Block the opponent's moves
# Flanking
# Piece count
# Threat analysis
# Piece placement
# Disrupt opponent's patterns
# Long-term planning
# Sacrifice for gain
from reversi import Reversi

center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
corner_squares = [(0, 0), (0, 7), (7, 0), (7, 7)]
edge_squares = [(i, 0) for i in range(8)] + \
               [(i, 7) for i in range(8)] + \
               [(0, j) for j in range(8)] + \
               [(7, j) for j in range(8)]

center_value = 10
corner_value = 50
edge_value = 5
mobility_value = 5


def heuristic1(player, game: Reversi):
    """ Control the center of the board """
    score = 0
    for square in center_squares:
        if game.board[square] == player:
            score += center_value
    return score


def heuristic2(player, game: Reversi):
    """ Control the edges of the board """
    score = 0
    for square in edge_squares:
        if game.board[square] == player:
            score += edge_value
    return score


def heuristic3(player, game: Reversi):
    """ Control the corners of the board """
    score = 0
    for square in corner_squares:
        if game.board[square] == player:
            score += corner_value
    return score


def heuristic4(player, game: Reversi):
    """ Mobility """
    score = (len(game.get_valid_moves(player)) - len(game.get_valid_moves(game.get_opponent(player)))) * mobility_value
    return score


def heuristic5(player, game: Reversi):
    """ Piece Count """
    counts = game.get_players_pieces()

    my_pieces = counts[player]
    opponent_pieces = counts[game.get_opponent(player)]
    score = len(my_pieces) - len(opponent_pieces)
    return score
