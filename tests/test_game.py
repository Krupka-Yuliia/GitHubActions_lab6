from tictactoe.game import create_board, make_move, check_winner, is_full, ai_move


def test_create_board():
    board = create_board()
    assert board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "Board should be empty 3x3 grid"


def test_make_move():
    board = create_board()
    assert make_move(board, 0, 0, "X") is True
    assert board[0][0] == "X"
    assert make_move(board, 0, 0, "O") is False, "Should not overwrite occupied cell"


def test_check_winner_row():
    board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
    assert check_winner(board) == "X"


def test_check_winner_col():
    board = [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]
    assert check_winner(board) == "O"


def test_check_winner_diag():
    board = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
    assert check_winner(board) == "X"


def test_no_winner():
    board = [["X", "O", "X"],
             ["O", "X", "O"],
             ["O", "X", "O"]]
    assert check_winner(board) is None


def test_is_full_true():
    board = [["X", "O", "X"],
             ["O", "X", "O"],
             ["O", "X", "O"]]
    assert is_full(board) is True


def test_is_full_false():
    board = [["X", "O", " "],
             ["O", "X", " "],
             ["O", " ", "O"]]
    assert is_full(board) is False


def test_ai_move_valid_coordinates():
    board = create_board()
    move = ai_move(board)
    assert move is not None, "AI should return a move when board not full"
    row, col = move
    assert 0 <= row <= 2 and 0 <= col <= 2, "AI move should be within board bounds"


def test_ai_move_empty_cell():
    board = [["X", "O", "X"],
             ["O", " ", "O"],
             ["X", "O", "X"]]
    move = ai_move(board)
    assert move == (1, 1), "AI should pick the only empty cell"


def test_ai_move_no_moves_left():
    board = [["X", "O", "X"],
             ["O", "X", "O"],
             ["O", "X", "X"]]
    assert ai_move(board) is None, "AI should return None when no empty cells left"
