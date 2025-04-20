# === Move ===
# Place a number if allowed.

def input_number(board, row, col, number):
    if board[row][col] != 0:
        print("Cell is already filled.")
        return False
    board[row][col] = number
    return True
