# Practical 05 Minimax
## Implementation of Minimax Algorithm for Two-Player Deterministic Games

## Aim
Implement the Minimax algorithm for two-player deterministic games.

## Problem statement
Understand and implement the basic Minimax algorithm for a two-player deterministic game. The notebook discusses adversarial search and examples such as Chess and Tic-Tac-Toe.

## Objectives
- Understand adversarial search in competitive environments.
- Represent possible moves using a game tree.
- Evaluate terminal states and select a move assuming the opponent also plays optimally.

## Theory
1. Adversarial search is used when players have conflicting goals. In a zero-sum game, one player’s gain is the other player’s loss.
2. Minimax assumes both players play optimally. MAX chooses the largest child value; MIN chooses the smallest child value.
3. Terminal game states are assigned utility values. In the included Tic-Tac-Toe example, X win = +1, O win = -1 and draw = 0.
4. The algorithm recursively explores possible moves, evaluates terminal states and propagates values back up the game tree.

## Algorithm / Procedure
1. Check whether the current board is a terminal state. If X wins, return +1; if O wins, return -1; if draw, return 0.
2. If it is MAX’s turn, try every empty cell as X and return the maximum recursive score.
3. If it is MIN’s turn, try every empty cell as O and return the minimum recursive score.
4. Undo each trial move before checking the next possibility.
5. For each legal move available to X, calculate its Minimax value and select the move with the highest score.

## Complexity / Practical nature
With branching factor b and search depth d, basic Minimax takes O(b^d) time. Recursive space is O(d), excluding the board representation and move-generation overhead.

## Expected output / record
For the included board, X has an immediate winning move at cell 7 (1-based indexing), so the program prints best move = 7 and score = +1.

## Python program
Source file: [`practical_05_minimax_tictactoe.py`](practical_05_minimax_tictactoe.py)

### Run
```bash
python practical_05_minimax_tictactoe.py
```

The program uses only Python's standard library; no external package installation is needed.

<!-- BEGIN FULL PYTHON SOURCE -->
## Complete Python code (copy-ready)

The same program is also saved as [`practical_05_minimax_tictactoe.py`](practical_05_minimax_tictactoe.py) so it can be run directly.

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

<!-- END FULL PYTHON SOURCE -->

## Oral / viva questions with answers
**Q1. What is Minimax?**
Answer: A decision algorithm for two-player games that maximizes the minimum guaranteed payoff.

**Q2. What is adversarial search?**
Answer: Search where an agent chooses actions while considering an opponent with conflicting goals.

**Q3. What is a game tree?**
Answer: A tree whose nodes are game states and whose edges represent legal moves.

**Q4. Who is MAX?**
Answer: The player who tries to maximize the utility value.

**Q5. Who is MIN?**
Answer: The opponent who tries to minimize the utility value.

**Q6. What is a utility function?**
Answer: A function that assigns a numerical value to a terminal or evaluated game state.

**Q7. What does zero-sum mean?**
Answer: One player’s gain is balanced by the other player’s loss.

**Q8. Why is recursion used?**
Answer: Each possible move creates a new game state, so the same evaluation procedure can be applied to the child state.

**Q9. What is the main limitation of Minimax?**
Answer: It can explore a very large game tree and become slow for games with high branching factors.

**Q10. What are the utility values used here?**
Answer: X win = +1, O win = -1 and draw = 0.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.
