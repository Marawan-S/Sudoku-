import numpy as np

Max_Strikes = 3  # Maximum number of allowed strikes

def load_labeled_sudoku():
    puzzle = np.array([
        [7, 2, 0, 0, 0, 1, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 1, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 9, 0, 0, 1, 0, 3],
        [0, 4, 0, 0, 0, 0, 9, 2, 0],
        [9, 0, 2, 1, 0, 8, 0, 7, 0],
        [2, 0, 0, 0, 0, 6, 0, 9, 0],
        [3, 9, 0, 0, 0, 7, 0, 0, 0],
        [6, 8, 0, 3, 0, 0, 5, 4, 1]
    ])

    solution = np.array([
        [7, 2, 3, 8, 9, 1, 6, 5, 4],
        [8, 6, 5, 2, 3, 4, 7, 1, 9],
        [4, 1, 9, 7, 6, 5, 8, 3, 2],
        [5, 7, 6, 9, 4, 2, 1, 8, 3],
        [1, 4, 8, 6, 7, 3, 9, 2, 5],
        [9, 3, 2, 1, 5, 8, 4, 7, 6],
        [2, 5, 1, 4, 8, 6, 3, 9, 7],
        [3, 9, 4, 5, 1, 7, 2, 6, 8],
        [6, 8, 7, 3, 2, 9, 5, 4, 1]
    ])

    return puzzle, solution

def display_board(board):
    print("\nCurrent Board:")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def input_number(board, row, col, number):
    if board[row][col] != 0:
        print("Cell is already filled.")
        return False
    board[row][col] = number
    return True

def check_end(current_board, solution_board):
    return np.array_equal(current_board, solution_board)

def main():
    game, solution = load_labeled_sudoku()
    strikes = 0
    used_moves = set()

    print("Welcome to Sudoku!")
    print("You have 3 strikes. Enter your move as: row col number (0-based index)")

    while True:
        display_board(game)
        print(f"Strikes: {strikes}/{Max_Strikes}")
        user_input = input("Your move (row col number) or 'q' to quit: ").strip()

        if user_input.lower() == 'q':
            print("Game exited.")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Invalid input. You must enter exactly 3 values: row col number.")
            strikes += 1
            if strikes >= Max_Strikes:
                print("Game over! Too many invalid attempts.")
                display_board(solution)
                print("Here is the correct solution.")
                break
            continue

        row, col, num = parts[0], parts[1], parts[2]

        if not (row.isdigit() and col.isdigit() and num.isdigit()):
            print("Only whole positive numbers are allowed.")
            strikes += 1
            if strikes >= Max_Strikes:
                print("Game over! Too many invalid attempts.")
                display_board(solution)
                print("Here is the correct solution.")
                break
            continue

        row, col, num = int(row), int(col), int(num)

        if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
            print("Row and column must be between 0 and 8. Number must be between 1 and 9.")
            strikes += 1
            if strikes >= Max_Strikes:
                print("Game over! Too many invalid attempts.")
                display_board(solution)
                print("Here is the correct solution.")
                break
            continue

        move_key = (row, col, num)
        if move_key in used_moves:
            print("You already entered this move before.")
            strikes += 1
            if strikes >= Max_Strikes:
                print("Game over! Too many repeated or invalid attempts.")
                display_board(solution)
                print("Here is the correct solution.")
                break
            continue
        used_moves.add(move_key)

        if solution[row][col] != num:
            print("Incorrect number.")
            strikes += 1
            if strikes >= Max_Strikes:
                print("Game over! Too many incorrect answers.")
                display_board(solution)
                print("Here is the correct solution.")
                break
            continue

        success = input_number(game, row, col, num)
        if not success:
            continue

        if check_end(game, solution):
            display_board(game)
            print("Congratulations! You solved the puzzle.")
            break

# Run the game
main()
