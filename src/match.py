from interface import print_board
from reversi import Reversi
import interface
from utils import read_move_player, minimax, do_best_move
import heuristics

pc1_heuristic = heuristics.piece_count
max_deph = 3


def player_vs_player():
    game = Reversi()
    while game.game_over():
        valid_moves = game.get_valid_moves()
        if not valid_moves:
            interface.no_valid_moves()
            continue
        interface.player_turn(game.current_player)
        print_board(game.board)
        interface.valid_moves(valid_moves)
        row, col = read_move_player()
        if (row, col) in valid_moves:
            game.make_move(row, col)
        else:
            interface.invalid_move()
    print_board(game.board)
    winner = game.get_winner()
    if winner == 0:
        interface.tie()
    else:
        interface.winner(winner)


def player_vs_pc():
    game = Reversi()
    while not game.game_over():
        valid_moves = game.get_valid_moves()
        if not valid_moves:
            interface.no_valid_moves()
            continue
        interface.player_turn(game.current_player)
        if game.current_player == 2:
            row, col = do_best_move(game, max_deph, game.current_player, pc1_heuristic)
            game.make_move(row, col)
            interface.player_put(game.opponent, row, col)
            continue
        print_board(game.board)
        interface.valid_moves(valid_moves)
        if game.current_player == 1:
            row, col = read_move_player()
            if (row, col) in valid_moves:
                game.make_move(row, col)
                interface.player_put(game.opponent, row, col)
            else:
                interface.invalid_move()

    print_board(game.board)
    winner = game.get_winner()
    if winner == 0:
        interface.tie()
    else:
        interface.winner(winner)
