
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

MAX_DEPTH = 3
PLAYER_1 = 1
PLAYER_2 = 2
PC_1 = 1
PC_2 = 2
