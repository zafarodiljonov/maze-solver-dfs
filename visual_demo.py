import os
import random
import time

from src.maze import solve_maze_dfs


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def generate_maze(width, height):
    if width < 5:
        width = 5
    if height < 5:
        height = 5

    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve(row, col):
        maze[row][col] = 0

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 1 <= new_row < height - 1 and 1 <= new_col < width - 1:
                if maze[new_row][new_col] == 1:
                    maze[row + dr // 2][col + dc // 2] = 0
                    carve(new_row, new_col)

    carve(1, 1)

    maze[1][1] = 0
    maze[height - 2][width - 2] = 0

    return maze


def print_maze(maze, start, end, visited=None, path=None, current=None):
    visited = visited or set()
    path = path or set()

    clear_screen()

    for row in range(len(maze)):
        line = ""

        for col in range(len(maze[0])):
            position = (row, col)

            if position == start:
                line += "S "
            elif position == end:
                line += "E "
            elif position == current:
                line += "@ "
            elif position in path:
                line += "* "
            elif position in visited:
                line += ". "
            elif maze[row][col] == 1:
                line += "█ "
            else:
                line += "  "

        print(line)


def is_valid_move(maze, row, col, visited):
    if row < 0 or col < 0:
        return False

    if row >= len(maze) or col >= len(maze[0]):
        return False

    if maze[row][col] == 1:
        return False

    if (row, col) in visited:
        return False

    return True


def dfs_visual(maze, start, end):
    visited = set()
    path = []

    def dfs(position):
        row, col = position

        if not is_valid_move(maze, row, col, visited):
            return False

        visited.add(position)
        path.append(position)

        print_maze(maze, start, end, visited, set(path), position)
        time.sleep(0.08)

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

        print_maze(maze, start, end, visited, set(path), position)
        time.sleep(0.08)

        return False

    dfs(start)
    return path, visited


def main():
    width = int(input("Enter maze width: "))
    height = int(input("Enter maze height: "))

    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    maze = generate_maze(width, height)

    start = (1, 1)
    end = (height - 2, width - 2)

    path, visited = dfs_visual(maze, start, end)

    print_maze(maze, start, end, set(visited), set(path))
    print("\nDFS complete.")
    print(f"Visited cells: {len(visited)}")
    print(f"Path length: {len(path)}")


if __name__ == "__main__":
    main()