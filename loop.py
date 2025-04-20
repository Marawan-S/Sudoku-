# === Loop ===
# Main game: take moves, check rules, show board.

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
