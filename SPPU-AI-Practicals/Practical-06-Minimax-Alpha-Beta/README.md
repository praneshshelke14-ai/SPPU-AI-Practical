# Practical 06 Minimax Alpha Beta
## Implementation of Minimax Algorithm with Alpha-Beta Pruning in AI

## Aim
Implement Minimax with Alpha-Beta Pruning to reduce computation time.

## Problem statement
Enhance Minimax using Alpha-Beta pruning to reduce computation time, as stated in Practical 6.

## Objectives
- Use recursion and backtracking in decision-making for games.
- Understand MAX and MIN nodes, game trees and utility values.
- Use alpha and beta bounds to remove branches that cannot affect the final decision.
- Understand that pruning improves efficiency without changing the Minimax result.

## Theory
1. Alpha-Beta pruning is an optimization of Minimax. It skips branches that cannot change the final decision.
2. Alpha (α) is the best value MAX can guarantee so far. It starts at negative infinity and can only increase.
3. Beta (β) is the best value MIN can guarantee so far. It starts at positive infinity and can only decrease.
4. When α >= β, the remaining children of the current node can be pruned.
5. The pruning result is the same as Minimax. The amount of work saved depends on move ordering.

## Algorithm / Procedure
1. Start with α = -infinity and β = +infinity.
2. At a MAX node, evaluate children, update the best value and α = max(α, best).
3. At a MIN node, evaluate children, update the best value and β = min(β, best).
4. Whenever α >= β, stop exploring the remaining children of that node.
5. Return the node’s Minimax value and select the move with the highest value for X.

## Complexity / Practical nature
Worst-case time remains O(b^d), similar to Minimax. With ideal move ordering, the effective search can approach O(b^(d/2)). Recursive space is O(d).

## Expected output / record
The program recommends cell 7 for X on the included example board, with score +1, and also reports the number of recursive nodes evaluated.

## Python program
Source file: [`practical_06_minimax_alpha_beta.py`](practical_06_minimax_alpha_beta.py)

### Run
```bash
python practical_06_minimax_alpha_beta.py
```

The program uses only Python's standard library; no external package installation is needed.

<!-- BEGIN FULL PYTHON SOURCE -->
## Complete Python code (copy-ready)

The same program is also saved as [`practical_06_minimax_alpha_beta.py`](practical_06_minimax_alpha_beta.py) so it can be run directly.

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

<!-- END FULL PYTHON SOURCE -->

## Oral / viva questions with answers
**Q1. What is Alpha-Beta pruning?**
Answer: An optimization that skips Minimax branches that cannot affect the final decision.

**Q2. What is alpha?**
Answer: The best lower-bound value MAX can guarantee so far.

**Q3. What is beta?**
Answer: The best upper-bound value MIN can guarantee so far.

**Q4. What is the pruning condition?**
Answer: Prune when alpha is greater than or equal to beta.

**Q5. Does pruning change the optimal move?**
Answer: No. It produces the same Minimax decision while evaluating fewer nodes.

**Q6. What are the initial alpha and beta values?**
Answer: Alpha = negative infinity and beta = positive infinity.

**Q7. Which node updates alpha?**
Answer: MAX nodes.

**Q8. Which node updates beta?**
Answer: MIN nodes.

**Q9. What is the worst-case time complexity?**
Answer: O(b^d), the same asymptotic bound as Minimax.

**Q10. When is pruning most effective?**
Answer: When the best moves are examined early, giving good move ordering.

## Source alignment note
This runnable Tic-Tac-Toe demonstration implements the Minimax + Alpha-Beta topic described in the supplied Practical 6 PDF. It is a complete teaching implementation and may be longer/different from the short illustrative code fragment in the manual.
