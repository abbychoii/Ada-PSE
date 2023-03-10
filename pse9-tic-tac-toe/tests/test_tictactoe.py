import pytest
from tictactoe_refactor import tic_tac_toe_winner
# from tictactoe import tic_tac_toe_winner

def test_tie():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]
    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'Tie'

def test_incomplete():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', '', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == None

def test_col_win():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'O', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'

def test_row_win():
    # Arrange
    board =[
        ['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'

def test_diag_win():
    # Arrange
    board =[
        ['O', 'O', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O']
    ]

    # Act
    result = tic_tac_toe_winner(board)

    # Assert
    assert result == 'O'