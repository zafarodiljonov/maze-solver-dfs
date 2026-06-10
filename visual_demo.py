import turtle
import time

maze = [
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,1,1,1,1,0,1,1,1,1,0,1,0],
    [0,1,0,0,0,0,0,0,0,1,0,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,0,0,0,1,1],
    [0,1,0,0,0,1,0,0,0,1,1,1,0,1,0],
    [0,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
    [0,0,0,0,0,0,1,1,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
]

start = (0, 0)
end = (14, 14)
cell_size = 28

delay = 0.08

screen = turtle.Screen()
screen.title("Live DFS Maze Solver")
screen.setup(600, 600)
screen.tracer(0)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

marker = turtle.Turtle()
marker.hideturtle()
marker.penup()
marker.speed(0)


def cell_to_screen(row, col):
    x = col * cell_size - 190
    y = 190 - row * cell_size
    return x, y


def draw_square(row, col, color):
    x, y = cell_to_screen(row, col)
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()

    for _ in range(4):
        drawer.forward(cell_size)
        drawer.right(90)

    drawer.end_fill()


def draw_dot(row, col, color):
    x, y = cell_to_screen(row, col)
    marker.goto(x + cell_size / 2, y - cell_size / 2)
    marker.dot(14, color)
    screen.update()
    time.sleep(delay)


def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                draw_square(row, col, "black")
            else:
                draw_square(row, col, "white")

    draw_square(start[0], start[1], "green")
    draw_square(end[0], end[1], "blue")
    screen.update()


def is_valid(row, col, visited):
    if row < 0 or col < 0:
        return False

    if row >= len(maze) or col >= len(maze[0]):
        return False

    if maze[row][col] == 1:
        return False

    if (row, col) in visited:
        return False

    return True


def live_dfs(row, col, visited, path):
    if not is_valid(row, col, visited):
        return False

    visited.add((row, col))
    path.append((row, col))

    draw_dot(row, col, "red")

    if (row, col) == end:
        return True

    moves = [
        (row + 1, col),
        (row, col + 1),
        (row - 1, col),
        (row, col - 1),
    ]

    for next_row, next_col in moves:
        if live_dfs(next_row, next_col, visited, path):
            return True

    draw_dot(row, col, "gray")
    path.pop()
    return False


draw_maze()

visited_cells = set()
final_path = []

live_dfs(start[0], start[1], visited_cells, final_path)

for row, col in final_path:
    draw_dot(row, col, "lime")

screen.mainloop()
