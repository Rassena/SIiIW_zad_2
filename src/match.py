from interface import print_board
from reversi import Reversi
import interface
from utils import read_move_player

def player_vs_player():
    game = Reversi()
    counter = 0
    while True:
        valid_moves = game.get_valid_moves()
        if not valid_moves:
            counter += 1
            if counter == 2:
                break
            else:
                interface.no_valid_moves()
                game.current_player = 3 - game.current_player
                continue
        counter = 0
        interface.player_turn(game.current_player)
        print_board(game.board)
        interface.valid_moves(valid_moves)
        while True:
            row, col = read_move_player()
            if (row, col) in valid_moves:
                game.make_move(row, col)
                break
            else:
                interface.invalid_move()
    print_board(game.board)
    winner = game.get_winner()
    if winner == 0:
        interface.tie()
    else:
        interface.winner(winner)