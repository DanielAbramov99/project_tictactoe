import random


# Function to display the game board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# Function to determine if a player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Function to determine if the game is a draw
def is_draw(board):
    return all(all(cell != " " for cell in row) for row in board)


# Function to allow players to choose their symbols
def get_symbols():
    while True:
        choice = input("Player 1, choose X or O (or type 'random' for a random choice): ").upper()
        if choice in ["X", "O"]:
            player1 = choice
            break
        elif choice == "RANDOM":
            player1 = random.choice(["X", "O"])
            break
        else:
            print("Invalid choice. Please choose 'X', 'O', or 'random'.")
    player2 = "O" if player1 == "X" else "X"
    print(f"Player 1 is {player1}, Player 2 is {player2}")
    return player1, player2


# Function that lets you start a new game
def start_new_game():
    while True:
        play_tic_tac_toe()
        replay = input("Would you like to play again? (yes/no): ").lower()
        if replay != "yes":
            print("have a nice day!")
            break


# Main function to play the game
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player1, player2 = get_symbols()
    current_player = player1
    while True:
        display_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
            if board[row][col] == " ":
                board[row][col] = current_player
                if is_winner(board, current_player):
                    display_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_draw(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                current_player = player2 if current_player == player1 else player1
            else:
                print("Cell already occupied, try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Invalid input. Please enter a number between 0 and 2.")


if __name__ == "__main__":
    start_new_game()

