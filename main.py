def solve_maze_dfs(maze, start, end, return_visited=False):
    visited = []
    visited_set = set()
    path = []

    def dfs(position):
        row, col = position

        if not is_valid_move(maze, row, col):
            return False

        if position in visited_set:
            return False

        visited_set.add(position)
        visited.append(position)
        path.append(position)

        if position == end:
            return True

        moves = [
            (row + 1, col),
            (row, col + 1),
            (row - 1, col),
            (row, col - 1),
        ]

        for next_position in moves:
            if dfs(next_position):
                return True

        path.pop()
        return False

    if dfs(start):
        if return_visited:
            return path, visited
        return path

    if return_visited:
        return [], visited
    return []

