from src.maze import is_valid_move


def test_open_cell_is_valid_move():
    maze = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]

    assert is_valid_move(maze, 0, 0) is True
