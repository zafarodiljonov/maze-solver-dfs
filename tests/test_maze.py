from src.maze import is_valid_move


def test_open_cell_is_valid_move():
    maze = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]

    assert is_valid_move(maze, 0, 0) is True

def test_wall_cell_is_invalid_move():
    maze = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]

    assert is_valid_move(maze, 0, 2) is False

def test_outside_maze_is_invalid_move():
    maze = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]

    assert is_valid_move(maze, -1, 0) is False
    assert is_valid_move(maze, 0, -1) is False
    assert is_valid_move(maze, 3, 0) is False
    assert is_valid_move(maze, 0, 3) is False
