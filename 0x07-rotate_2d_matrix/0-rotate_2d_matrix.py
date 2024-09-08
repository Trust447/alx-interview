#!/usr/bin/python3
"""Module for rotating a 2D matrix 90 degrees clockwise."""


def transpose_matrix(matrix, n):
    """Transposes the given matrix in place.

    Args:
        matrix (list of list of int): The 2D matrix to be transposed.
        n (int): The dimension of the square matrix.
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """Reverses each row of the given matrix in place.

    Args:
        matrix (list of list of int): The 2D matrix whose rows will be reversed.
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to be rotated.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    transpose_matrix(matrix, n)

    # Step 2: Reverse each row of the transposed matrix
    reverse_matrix(matrix)
