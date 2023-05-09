


def print_board(board):
    print("   0 1 2 3 4 5 6 7 ")
    print("  +-+-+-+-+-+-+-+-+")
    for row in range(8):
        print(row, end=" |")
        for col in range(8):
            if board[row][col] == 0:
                print(" ", end="|")
            elif board[row][col] == 1:
                print("X", end="|")
            else:
                print("O", end="|")
        print("\n  +-+-+-+-+-+-+-+-+")