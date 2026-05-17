# Function to print the board
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Function to check safe position
def is_safe(board, row, col):

    for i in range(row):

        # Check same column
        if board[i] == col:
            return False

        # Check diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve_nqueen(board, row, n):

    # All queens placed
    if row == n:
        print("\nSolution Found:\n")
        print_board(board, n)
        return True

    # Try every column
    for col in range(n):

        if is_safe(board, row, col):

            # Place queen
            board[row] = col

            # Recursive call
            if solve_nqueen(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1

    return False


# Main Program
n = int(input("Enter number of queens: "))

# Initialize board
board = [-1] * n

if not solve_nqueen(board, 0, n):
    print("No Solution Exists")