import builtins
import pytest
from tictactoe.game import (
    create_board,
    make_move,
    check_winner,
    is_full,
    ai_move,
    print_board,
    play_game,
)


def test_create_board():
    board = create_board()
    assert board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "Board should be empty 3x3 grid"


def test_make_move():
    board = create_board()
    assert make_move(board, 0, 0, "X")
    assert board[0][0] == "X"
    assert not make_move(board, 0, 0, "O")


def test_check_winner_row():
    assert check_winner([["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]) == "X"


def test_check_winner_col():
    assert check_winner([["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]) == "O"


def test_check_winner_diag():
    assert check_winner([["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]) == "X"


def test_no_winner():
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert check_winner(board) is None


def test_is_full_true():
    assert is_full([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]])


def test_is_full_false():
    assert not is_full([["X", "O", " "], ["O", "X", " "], ["O", " ", "O"]])


def test_ai_move_valid_coordinates():
    board = create_board()
    row, col = ai_move(board)
    assert 0 <= row <= 2 and 0 <= col <= 2


def test_ai_move_empty_cell():
    board = [["X", "O", "X"], ["O", " ", "O"], ["X", "O", "X"]]
    assert ai_move(board) == (1, 1)


def test_ai_move_no_moves_left():
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]
    assert ai_move(board) is None


def test_print_board(capsys):
    board = [["X", "O", " "], [" ", "X", " "], ["O", " ", "X"]]
    print_board(board)
    output = capsys.readouterr().out
    assert "|" in output and "X" in output and "O" in output


def test_play_game_invalid_input(monkeypatch, capsys):
    inputs = iter(["1", "a", "0", "0", "0", "1"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr("tictactoe.game.ai_move", lambda b: None)
    with pytest.raises(StopIteration):
        play_game()
    assert "Please enter numbers between 0 and 2." in capsys.readouterr().out
