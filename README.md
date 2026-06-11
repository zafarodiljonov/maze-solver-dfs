# Maze Solver DFS

A Python project that solves mazes using the Depth-First Search (DFS) algorithm.

## Team Members

* Team Leader: Zafar Odijonov
* Team Member Javokhir
* Team Member Azizbek

## Project Description

This project represents a maze as a grid where:

* `0` = Open path
* `1` = Wall

The program uses the Depth-First Search (DFS) algorithm to find a path from a start position to an end position.

The project was developed using:

* Python
* Git
* GitHub
* Test-Driven Development (TDD)
* Unit Testing with pytest

## Features

* Maze represented as a 2D grid
* Start and end positions
* DFS maze solving algorithm
* Visited cell tracking
* Boundary validation
* Invalid start/end handling
* Automated unit tests
* Live DFS visualization

## Project Structure

```text
maze-solver-dfs/
│
├── main.py
├── visual_demo.py
├── README.md
│
├── src/
│   ├── __init__.py
│   └── maze.py
│
└── tests/
    └── test_maze.py
```

## Running the Tests

```bash
python -m pytest
```

Expected output:

```text
9 passed
```

## Running the Console Demo

```bash
python main.py
```

This displays:

* Visited cells
* Final DFS path

## Running the Visual DFS Animation

```bash
python visual_demo.py
```

The animation shows:

* DFS exploring the maze
* Visited cells
* Backtracking
* Final path to the exit

## Test Cases

The project includes tests for:

1. Open cell validation
2. Wall validation
3. Boundary validation
4. DFS path finding
5. Unsolvable maze handling
6. Start equals end
7. Invalid start position
8. Invalid end position
9. Visited cell tracking

## Git Workflow Used

1. Clone repository
2. Create feature branch
3. Write tests first (TDD)
4. Commit changes
5. Push branch
6. Create Pull Request
7. Review and merge into main

## Algorithm

Depth-First Search (DFS) explores one path as deeply as possible before backtracking and trying alternative paths.


## Internship Project

This project was completed by a 3-member internship team in 5 days using GitHub collaboration and Test-Driven Development.

