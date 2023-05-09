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
piece_value = 1

def control_center(game: Reversi, player):
    """ Control the center of the board """
    score = game.get_player_pieces() * piece_value
    for square in center_squares:
        if game.board[square] == player:
            score += center_value
    return score


def control_edge(game: Reversi, player):
    """ Control the edges of the board """
    score = game.get_player_pieces() * piece_value
    for square in edge_squares:
        if game.board[square] == player:
            score += edge_value
    return score


def control_corners(game: Reversi, player):
    """ Control the corners of the board """
    score = game.get_player_pieces() * piece_value
    for square in corner_squares:
        if game.board[square] == player:
            score += corner_value
    return score


def mobility(game: Reversi, player):
    """ Mobility """
    score = game.get_player_pieces() * piece_value
    score += (len(game.get_valid_moves(player)) - len(game.get_valid_moves(game.get_opponent(player)))) * mobility_value
    return score


def piece_count(game: Reversi, player):
    """ Piece Count """
    counts = game.get_players_pieces()
    my_pieces = counts[player]
    opponent_pieces = counts[game.get_opponent(player)]
    score = my_pieces - opponent_pieces
    return score
