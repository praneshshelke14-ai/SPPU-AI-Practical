# AI Practicals 1-9 - Complete Python Code Listings

This document contains the complete source code for every practical in the supplied set that is a programming practical (Practicals 1-6). Each program is also saved as a standalone `.py` file in its practical folder and embedded in that folder README.

**Practicals 7-9 are tool-based assignments in the supplied lab material** (ChatGPT, Sora and AI Image Generator). The source documents describe practical use, prompts and observations rather than a required Python program. Their activity sheets are included separately; this repository does not mislabel unrelated scripts as required practical code.

## Practical 1 - Rule-Based Expert System

File: `Practical-01-Expert-System/practical_01_rule_based_expert_system.py`

```python
"""Practical 1: Rule-Based Expert System (RBS) for simple computer troubleshooting.

This is a small educational rule-based system. It is not a professional diagnostic tool.
"""

RULES = [
    ({"power_on": False},
     "The computer does not power on. Check the wall socket, power cable, adapter and battery."),
    ({"power_on": True, "display_visible": False},
     "The computer powers on but shows no display. Check brightness, display cable and external monitor."),
    ({"power_on": True, "display_visible": True, "internet_working": False},
     "The display works but internet does not. Check Wi-Fi/Ethernet, router and network settings."),
    ({"power_on": True, "display_visible": True, "internet_working": True},
     "The basic checks are normal. The system appears to be working."),
]


def ask_yes_no(question):
    """Read a yes/no answer and return True for yes, False for no."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def infer(facts):
    """Apply the first rule whose conditions match the known facts."""
    for conditions, conclusion in RULES:
        if all(facts.get(key) == value for key, value in conditions.items()):
            return conclusion
    return "Not enough information. Please collect more facts."


def main():
    print("RULE-BASED EXPERT SYSTEM - COMPUTER TROUBLESHOOTING")
    facts = {"power_on": ask_yes_no("Does the computer power on?")}

    if facts["power_on"]:
        facts["display_visible"] = ask_yes_no("Is anything visible on the display?")
        if facts["display_visible"]:
            facts["internet_working"] = ask_yes_no("Is the internet connection working?")

    print("\nKnown facts:", facts)
    print("Expert-system advice:", infer(facts))


if __name__ == "__main__":
    main()
```

## Practical 2 - BFS and DFS Maze Solver

File: `Practical-02-BFS-DFS-Maze/practical_02_bfs_dfs_maze_solver.py`

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

## Practical 3 - A* Search

File: `Practical-03-A-Star-Search/practical_03_a_star_search.py`

```python
"""Practical 3: A* graph search using f(n) = g(n) + h(n)."""
import heapq

# Weighted undirected graph: neighbour -> travel cost
GRAPH = {
    "S": {"A": 2, "B": 4},
    "A": {"S": 2, "C": 2, "D": 6},
    "B": {"S": 4, "C": 1},
    "C": {"A": 2, "B": 1, "G": 3},
    "D": {"A": 6, "G": 1},
    "G": {"C": 3, "D": 1},
}

# Estimated remaining cost to goal G. This example uses an admissible heuristic.
HEURISTIC = {"S": 5, "A": 4, "B": 3, "C": 2, "D": 1, "G": 0}


def a_star(start, goal):
    if start not in GRAPH or goal not in GRAPH:
        raise ValueError("Start and goal must be graph vertices")

    # Heap items are (f_score, g_score, vertex).
    open_heap = [(HEURISTIC[start], 0, start)]
    g_cost = {start: 0}
    parent = {start: None}

    while open_heap:
        f_score, cost_so_far, current = heapq.heappop(open_heap)
        # Ignore outdated heap entries after a better route has been found.
        if cost_so_far != g_cost.get(current):
            continue
        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path)), g_cost[goal]

        for neighbour, edge_cost in GRAPH[current].items():
            new_cost = cost_so_far + edge_cost
            if new_cost < g_cost.get(neighbour, float("inf")):
                g_cost[neighbour] = new_cost
                parent[neighbour] = current
                new_f = new_cost + HEURISTIC[neighbour]
                heapq.heappush(open_heap, (new_f, new_cost, neighbour))

    return None, float("inf")


def main():
    start, goal = "S", "G"
    path, cost = a_star(start, goal)
    print(f"A* search from {start} to {goal}")
    if path is None:
        print("No path found.")
    else:
        print("Best path:", " -> ".join(path))
        print("Total path cost:", cost)


if __name__ == "__main__":
    main()
```

## Practical 4 - Constraint Satisfaction Problem

File: `Practical-04-Constraint-Satisfaction/practical_04_csp_map_coloring.py`

```python
"""Practical 4: Map colouring as a CSP using backtracking, MRV, LCV and forward checking."""

VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
COLORS = ["Red", "Green", "Blue"]
NEIGHBORS = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

assignment = {}


def legal_values(variable):
    used = {assignment[n] for n in NEIGHBORS[variable] if n in assignment}
    return [color for color in COLORS if color not in used]


def select_mrv():
    """Minimum Remaining Values: select the variable with fewest legal colours."""
    unassigned = [v for v in VARIABLES if v not in assignment]
    return min(unassigned, key=lambda v: (len(legal_values(v)), -len(NEIGHBORS[v])))


def order_lcv(variable, values):
    """Least Constraining Value: try the colour that removes fewest neighbour options."""
    def impact(color):
        affected = 0
        for neighbour in NEIGHBORS[variable]:
            if neighbour not in assignment and color in legal_values(neighbour):
                affected += 1
        return affected
    return sorted(values, key=impact)


def forward_check():
    """Fail early if any unassigned variable has no remaining legal colour."""
    return all(legal_values(v) for v in VARIABLES if v not in assignment)


def backtrack():
    if len(assignment) == len(VARIABLES):
        return True

    variable = select_mrv()
    for color in order_lcv(variable, legal_values(variable)):
        assignment[variable] = color
        if forward_check() and backtrack():
            return True
        del assignment[variable]  # undo assignment (backtracking)
    return False


def main():
    if backtrack():
        print("Map-colouring solution:")
        for region in VARIABLES:
            print(f"{region}: {assignment[region]}")
        print("\nConstraint check:", all(
            assignment[a] != assignment[b]
            for a in VARIABLES for b in NEIGHBORS[a]
        ))
    else:
        print("No solution exists with the selected colours.")


if __name__ == "__main__":
    main()
```

## Practical 5 - Minimax

File: `Practical-05-Minimax/practical_05_minimax_tictactoe.py`

```python
"""Practical 5: Minimax algorithm for a two-player deterministic game (Tic-Tac-Toe).

X is the maximizer (+1); O is the minimizer (-1). The board is indexed 0..8.
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def minimax(board, is_maximizing):
    result = winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False)
                board[i] = " "  # undo the trial move
                best = max(best, score)
        return best

    best = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, True)
            board[i] = " "  # undo the trial move
            best = min(best, score)
    return best


def best_move(board):
    best_score = float("-inf")
    selected = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score, selected = score, i
    return selected, best_score


def print_board(board):
    for r in range(0, 9, 3):
        print(" | ".join(board[r:r + 3]))
        if r < 6:
            print("---------")


def main():
    # Demonstration state: X can win immediately by placing at cell 7 (1-based).
    board = ["X", "O", "X", "O", "X", " ", " ", " ", "O"]
    print("Current Tic-Tac-Toe board:")
    print_board(board)
    move, score = best_move(board)
    if move is None:
        print("No legal move available.")
    else:
        print(f"Best move for X: cell {move + 1}")
        print("Minimax score:", score)


if __name__ == "__main__":
    main()
```

## Practical 6 - Minimax with Alpha-Beta Pruning

File: `Practical-06-Minimax-Alpha-Beta/practical_06_minimax_alpha_beta.py`

```python
"""Practical 6: Minimax with Alpha-Beta pruning for Tic-Tac-Toe.

The algorithm gives the same optimal decision as Minimax while skipping branches
that cannot affect the final choice. X maximizes and O minimizes.
"""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]
nodes_visited = 0


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def minimax_alpha_beta(board, is_maximizing, alpha, beta):
    global nodes_visited
    nodes_visited += 1

    result = winner(board)
    if result == "X":
        return 1
    if result == "O":
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                value = minimax_alpha_beta(board, False, alpha, beta)
                board[i] = " "  # undo the trial move
                best = max(best, value)
                alpha = max(alpha, best)
                if alpha >= beta:
                    break  # beta cutoff: remaining children cannot improve MIN's choice
        return best

    best = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            value = minimax_alpha_beta(board, True, alpha, beta)
            board[i] = " "  # undo the trial move
            best = min(best, value)
            beta = min(beta, best)
            if alpha >= beta:
                break  # alpha cutoff
    return best


def best_move(board):
    global nodes_visited
    nodes_visited = 0
    best_score = float("-inf")
    selected = None
    alpha, beta = float("-inf"), float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax_alpha_beta(board, False, alpha, beta)
            board[i] = " "
            if score > best_score:
                best_score, selected = score, i
            alpha = max(alpha, best_score)
    return selected, best_score


def print_board(board):
    for r in range(0, 9, 3):
        print(" | ".join(board[r:r + 3]))
        if r < 6:
            print("---------")


def main():
    board = ["X", "O", "X", "O", "X", " ", " ", " ", "O"]
    print("Current Tic-Tac-Toe board:")
    print_board(board)
    move, score = best_move(board)
    print(f"Best move for X: cell {move + 1}" if move is not None else "No legal move.")
    print("Alpha-Beta score:", score)
    print("Recursive nodes evaluated:", nodes_visited)


if __name__ == "__main__":
    main()
```
