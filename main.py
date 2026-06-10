from src.maze import solve_maze_dfs

maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
]

start = (0, 0)
end = (3, 3)

path, visited = solve_maze_dfs(
    maze,
    start,
    end,
    return_visited=True
)

print("Visited Cells:")
for cell in visited:
    print(cell)

print("\nFinal Path:")
for cell in path:
    print(cell)
