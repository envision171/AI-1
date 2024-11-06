def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    # If all queens are placed, return True
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen at board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens(board, col + 1, n):
                return True

            # Backtrack if placing queen doesn't lead to a solution
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n):
        print_board(board)
    else:
        print("No solution exists")

# Example usage for 4-queens problem
n_queens(4)
