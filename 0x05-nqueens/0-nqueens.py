#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def generate_solutions(row, column):
    """Generate all valid solutions for placing queens."""
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """Place a queen on the board in a safe position."""
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """Check if the queen can be safely placed."""
    if x in array:
        return False
    return all(abs(array[column] - x) != q - column for column in range(q))


def init():
    """Initialize the board and check for valid input."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """Execute the N-Queens solution."""
    n = init()
    # Generate all solutions
    solutions = generate_solutions(n, n)
    # Print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
