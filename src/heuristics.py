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
from reversi import Reversi, get_opponent

CENTER_SQUARES = [(3, 3), (3, 4), (4, 3), (4, 4)]
CORNER_SQUARES = [(0, 0), (0, 7), (7, 0), (7, 7)]
EDGE_SQUARES = [(i, 0) for i in range(8)] + \
               [(i, 7) for i in range(8)] + \
               [(0, j) for j in range(8)] + \
               [(7, j) for j in range(8)]

CENTER_VALUE = 10
CORNER_VALUE = 50
EDGE_VALUE = 5
MOBILITY_VALUE = 5
BASE_PIECE_VALUE = 1

def control_center(game: Reversi, player):
    """ Control the center of the board """
    score = game.get_player_pieces() * BASE_PIECE_VALUE
    for square in CENTER_SQUARES:
        if game.board[square] == player:
            score += CENTER_VALUE
    return score


def control_edge(game: Reversi, player):
    """ Control the edges of the board """
    score = game.get_player_pieces() * BASE_PIECE_VALUE
    for square in EDGE_SQUARES:
        if game.board[square] == player:
            score += EDGE_VALUE
    return score


def control_corners(game: Reversi, player):
    """ Control the corners of the board """
    score = game.get_player_pieces() * BASE_PIECE_VALUE
    for square in CORNER_SQUARES:
        if game.board[square] == player:
            score += CORNER_VALUE
    return score


def mobility(game: Reversi, player):
    """ Mobility """
    score = game.get_player_pieces() * BASE_PIECE_VALUE
    score += (len(game.get_valid_moves(player)) - len(game.get_valid_moves(game.get_opponent(player)))) * MOBILITY_VALUE
    return score


def piece_count(game: Reversi, player):
    """ Piece Count """
    counts = game.get_players_pieces()
    my_pieces = counts[player]
    opponent_pieces = counts[get_opponent(player)]
    score = my_pieces - opponent_pieces
    return score
