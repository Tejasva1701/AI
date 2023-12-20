# Write a program to implement the 8-queen Problem

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_queens(board, row + 1):
                return True
            # backtrack step
            board[row][col] = 0

    return False

def print_solution(board):
    for row in board:
        print("  ".join(["Q" if cell == 1 else "." for cell in row]))

def main():
    board_size = 8
    chess_board = [[0 for _ in range(board_size)] for _ in range(board_size)]

    if solve_queens(chess_board, 0):
        print_solution(chess_board)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()


# Sample output
# .  Q  .  .
# .  .  .  Q
# Q  .  .  .
# .  .  Q  .