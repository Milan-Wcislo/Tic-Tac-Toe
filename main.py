tic_tac_toe = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]


# Correctly Prints Tic Tac Toe
def print_tic_tac_toe():
    print("\n")
    for row in range(3):
        if row % 3 == 0:
            print(f"{((row + 1) * 3) - 2}  {tic_tac_toe[row * 3]} | {tic_tac_toe[row * 3 + 1]} | {tic_tac_toe[row * 3 + 2]}")
        else:
            print("  ---+---+---")
            print(f"{(row + 1) * 3 - 2}  {tic_tac_toe[row * 3]} | {tic_tac_toe[row * 3 + 1]} | {tic_tac_toe[row * 3 + 2]}")
    print("\n")        


# Function to check for a winning position
def check_winning_position(board):
    for combination in winning_combinations:
        if all(board[i] == "X" for i in combination):
            return True
        if all(board[i] == "O" for i in combination):
            return True
    return None


symbol_check = 0

while True:
    print_tic_tac_toe()

    symbol_check += 1

    if symbol_check % 2 == 0:
        symbol = "X"
    else:
        symbol = "O"

    while True:
        try:
            user = int(input(f"It's {symbol} Turn: ").upper())
        except ValueError:
            print("Error: Wrong Value! Please Type the Number Beetwen 1 and 9")
            continue

        try:
            answer = tic_tac_toe[user - 1]
        except IndexError:
            print("Error: Wrong Number! Please Type the Number Beetwen 1 and 9")
            continue

        if answer == " ":
            tic_tac_toe[user - 1] = symbol
            break
        else:
            print("Error: This Area has Taken")

    if check_winning_position(tic_tac_toe) == True:
        print_tic_tac_toe()
        print(f"{symbol} win!")
        break
