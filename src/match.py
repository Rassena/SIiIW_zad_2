from interface import print_board
from reversi import Reversi, get_opponent
import interface
from utils import read_move_player, do_best_move
import heuristics

pc1_heuristic = heuristics.piece_count
MAX_DEPTH = 3
PLAYER_1 = 1
PLAYER_2 = 2
PC_1 = 1
PC_2 = 2

def player_vs_player():
    game = Reversi()
    current_player = PLAYER_1
    while not game.game_over():
        valid_moves = game.get_valid_moves(current_player)
        if not valid_moves:
            interface.no_valid_moves(current_player)
            current_player = get_opponent(current_player)
            continue
        interface.player_turn(current_player)
        print_board(game.board)
        interface.count(*game.get_players_pieces()[1:])
        interface.valid_moves(valid_moves, current_player)
        row, col = read_move_player()
        while (row, col) not in valid_moves:
            interface.invalid_move()
            row, col = read_move_player()
        game.make_move(row, col, current_player)
        current_player = get_opponent(current_player)
    print_board(game.board)
    winner = game.get_winner()
    if winner == 0:
        interface.tie()
    else:
        interface.winner(winner)
        interface.count(PLAYER_1, PLAYER_2)


def player_vs_pc(evaluate, pc=PC_2):
    game = Reversi()
    current_player = PLAYER_1
    while not game.game_over():
        valid_moves = game.get_valid_moves(current_player)
        if not valid_moves:
            interface.no_valid_moves(current_player)
            current_player = get_opponent(current_player)
            continue
        interface.player_turn(current_player)
        print_board(game.board)
        interface.count(*game.get_players_pieces()[1:])
        interface.valid_moves(valid_moves, current_player)
        if current_player != pc:
            row, col = read_move_player()
            while (row, col) not in valid_moves:
                interface.invalid_move()
                row, col = read_move_player()
        else:
            row, col = do_best_move(game, MAX_DEPTH, current_player, evaluate)
        game.make_move(row, col, current_player)
        interface.player_put(current_player, row, col)
        current_player = get_opponent(current_player)
    print_board(game.board)
    winner = game.get_winner()
    if winner == 0:
        interface.tie()
    else:
        interface.winner(winner)
        interface.count(PLAYER_1, PLAYER_2)
