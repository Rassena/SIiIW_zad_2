import copy

from reversi import Reversi
import heuristics


def read_move_player():
    while True:
        try:
            row, col = map(int, input("Enter row and column: ").split())
        except ValueError:
            print("invalid value!")
            continue
        return row, col


def evaluate(game: Reversi, player):
    player_score = heuristics.piece_count(game, player)
    opponent_score = heuristics.piece_count(game, game.get_opponent(player))
    return player_score - opponent_score


def do_best_move(game_state:Reversi, depth, player, evaluate):
    moves = game_state.get_valid_moves()
    best_move = moves[0]
    best_value = float('-inf')
    for move in moves[1:]:
        new_game = copy.deepcopy(game_state)
        new_game.make_move(move[0], move[1], player)
        value = minimax(new_game, depth - 1, player, False, evaluate)
        if value > best_value:
            best_move = move
            best_value = value
    return best_move

def minimax(game_state:Reversi, depth, player, max_player, evaluate):
    if depth == 0 or game_state.game_over():
        return evaluate(game_state, player)

    if max_player:
        value = float('-inf')
        for move in game_state.get_valid_moves(player):
            new_game_state = copy.deepcopy(game_state)
            new_game_state.make_move(move[0], move[1])
            value = max(value, minimax(new_game_state, depth - 1, player, False, evaluate))
        return value
    else:
        value = float('inf')
        for move in game_state.get_valid_moves(game_state.opponent):
            new_node = copy.deepcopy(game_state)
            new_node.make_move(move[0], move[1], opponent=True)
            value = min(value, minimax(new_node, depth - 1, player, True, evaluate))
        return value
