
def read_move_player():
    while True:
        try:
            row, col = map(int, input("Enter row and column: ").split())
        except ValueError:
            print("invalid value!")
            continue
        return row, col
