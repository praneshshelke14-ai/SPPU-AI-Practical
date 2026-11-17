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
