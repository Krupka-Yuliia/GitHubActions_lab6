import random


def ai_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if not empty_cells:
        return None
    return random.choice(empty_cells)


def create_board():
    return [[" "] * 3 for _ in range(3)]


def print_board(board):
    for row in board:
        print("|".join(row))
    print()


def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def play_game():
    print("Welcome to Tic Tac Toe!")
    mode = input("Choose mode: 1 - Two Players, 2 - vs Computer: ").strip()

    board = create_board()
    player = "X"

    while True:
        print_board(board)

        if mode == "2" and player == "O":
            print("AI is making a move...")
            move = ai_move(board)
            if move is None:
                print("It's a tie!")
                break
            row, col = move
        else:
            try:
                row = int(input(f"Player {player}, enter row (0-2): "))
                col = int(input(f"Player {player}, enter col (0-2): "))
            except ValueError:
                print("Please enter numbers between 0 and 2.")
                continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be between 0 and 2.")
            continue

        if make_move(board, row, col, player):
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"🎉 Player {winner} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move, cell already taken. Try again.")


if __name__ == "__main__":
    play_game()
