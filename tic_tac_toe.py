# for player symbols
PLAYER_X = "X"
PLAYER_O = "O"

# main function to start the game
def main():
    # Print a welcome message and instructions
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X  |  Player 2: O")
    print("Let's start!")

    # Create the game board
    board = [" " for _ in range(9)]  # list to represent the board

    # Print the initial board state
    print_board(board)

    # Start the game loop
    current_player = PLAYER_X
    while True:
        # Get player's move
        move = get_move(board, current_player)

        # Update the board with the player's move
        board[move] = current_player

        # Print updated board state
        print_board(board)

        # Check for win or draw
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# function to print the game board
def print_board(board):
    # Print the board with row and column indices
    for i in range(3):
        print("|".join(board[i * 3:i * 3 + 3]))
        if i < 2:
            print("-" * 5)

# function to get player's move
def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                return move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# function to check for win
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# function to check for draw
def check_draw(board):
    return " " not in board

# Call the main function to start the game
if __name__ == "__main__":
    main()
