# === Wincheck ===
# Check if the puzzle is solved.

def check_end(current_board, solution_board):
    return np.array_equal(current_board, solution_board)
