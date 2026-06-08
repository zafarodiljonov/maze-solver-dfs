def is_valid_move(maze, row, col):
    if row < 0 or col < 0:
        return False

    if row >= len(maze) or col >= len(maze[0]):
        return False

    return maze[row][col] == 0
