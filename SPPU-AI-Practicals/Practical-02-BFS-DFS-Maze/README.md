# Practical 02 BFS DFS Maze
## Implementation of Search Algorithms (BFS and DFS) for Maze Solving

## Aim
Implement BFS and DFS maze solvers using graph search.

## Problem statement
Implement AI search algorithms BFS and DFS to solve a maze, as written in the Practical 2 notebook.

## Objectives
- Understand graph traversal and search.
- Implement Breadth-First Search and Depth-First Search.
- Compare the routes found by BFS and DFS in a maze.

## Theory
1. A maze can be represented as a graph: each open cell is a vertex and each legal move is an edge.
2. BFS explores nodes level by level using a queue. In an unweighted maze, BFS finds a path with the minimum number of moves.
3. DFS explores one branch deeply before backtracking, typically using a stack or recursion. DFS can find a route but does not guarantee a shortest route.
4. A visited set prevents repeated exploration and infinite loops. A parent map is used to reconstruct the path.

## Algorithm / Procedure
1. Find the start cell S and goal cell E.
2. Treat every non-wall cell as a graph vertex and connect up, down, left and right neighbours.
3. For BFS, place S in a queue. For DFS, place S on a stack.
4. Remove the next cell from the frontier. If it is E, reconstruct the path using parent links.
5. Add every valid unvisited neighbour to the frontier and record its parent.
6. Repeat until E is reached or the frontier becomes empty.

## Complexity / Practical nature
For V open cells and E legal neighbour connections, both BFS and DFS take O(V + E) time and O(V) auxiliary space. In a grid maze, V is at most rows x columns.

## Expected output / record
The program prints a route and move count for both BFS and DFS and shows the route cells marked with *.

## Python program
Source file: [`practical_02_bfs_dfs_maze_solver.py`](practical_02_bfs_dfs_maze_solver.py)

### Run
```bash
python practical_02_bfs_dfs_maze_solver.py
```

The program uses only Python's standard library; no external package installation is needed.

<!-- BEGIN FULL PYTHON SOURCE -->
## Complete Python code (copy-ready)

The same program is also saved as [`practical_02_bfs_dfs_maze_solver.py`](practical_02_bfs_dfs_maze_solver.py) so it can be run directly.

```python
"""Practical 2: Solve a maze using Breadth-First Search (BFS) and Depth-First Search (DFS)."""
from collections import deque

MAZE = [
    "S...#",
    ".##.#",
    "...#.",
    "##...",
    "....E",
]
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
ROWS, COLS = len(MAZE), len(MAZE[0])


def find_symbol(symbol):
    for r in range(ROWS):
        for c in range(COLS):
            if MAZE[r][c] == symbol:
                return (r, c)
    raise ValueError(f"Maze is missing {symbol!r}")


START, GOAL = find_symbol("S"), find_symbol("E")


def is_open(cell):
    r, c = cell
    return 0 <= r < ROWS and 0 <= c < COLS and MAZE[r][c] != "#"


def restore_path(parent, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return list(reversed(path))


def search(use_bfs=True):
    """Return a path from S to E, or None if no route exists."""
    frontier = deque([START]) if use_bfs else [START]
    parent = {START: None}  # also acts as the visited set

    while frontier:
        current = frontier.popleft() if use_bfs else frontier.pop()
        if current == GOAL:
            return restore_path(parent, GOAL)

        r, c = current
        for dr, dc in DIRECTIONS:
            nxt = (r + dr, c + dc)
            if is_open(nxt) and nxt not in parent:
                parent[nxt] = current
                frontier.append(nxt)
    return None


def show_maze(path=None):
    path_cells = set(path[1:-1]) if path else set()
    for r, row in enumerate(MAZE):
        print("".join("*" if (r, c) in path_cells else ch
                      for c, ch in enumerate(row)))


def main():
    for name, use_bfs in (("BFS", True), ("DFS", False)):
        path = search(use_bfs)
        print(f"\n{name} result:")
        if path is None:
            print("No path exists.")
        else:
            print("Path:", " -> ".join(map(str, path)))
            print("Number of moves:", len(path) - 1)
            show_maze(path)


if __name__ == "__main__":
    main()
```

<!-- END FULL PYTHON SOURCE -->

## Oral / viva questions with answers
**Q1. What is a graph?**
Answer: A set of vertices connected by edges.

**Q2. What is BFS?**
Answer: Breadth-First Search explores all neighbours at the current depth before moving deeper.

**Q3. Which data structure is used by BFS?**
Answer: A queue (FIFO).

**Q4. What is DFS?**
Answer: Depth-First Search explores one branch as far as possible before backtracking.

**Q5. Which data structure is used by iterative DFS?**
Answer: A stack (LIFO).

**Q6. Which algorithm finds the shortest path in an unweighted graph?**
Answer: BFS.

**Q7. Does DFS always find the shortest path?**
Answer: No. It finds a path if one exists, but the path may not be shortest.

**Q8. Why is a visited set required?**
Answer: To avoid processing the same cell repeatedly and prevent cycles.

**Q9. What is the purpose of the parent dictionary?**
Answer: It stores the predecessor of each discovered cell so that the path can be reconstructed.

**Q10. What is the time complexity of BFS and DFS?**
Answer: O(V + E) using adjacency-list-style traversal.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.
