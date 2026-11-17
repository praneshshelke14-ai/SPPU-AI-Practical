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
