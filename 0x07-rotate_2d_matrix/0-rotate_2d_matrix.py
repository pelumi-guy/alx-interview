#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix) -> None:
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
        - Do not return anything. The matrix must be edited in-place.
        - You can assume the matrix will have
            2 dimensions and will not be empty.
    """
    # Transposing the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)

    # Reverse rows of matrix
    for row in matrix:
        row.reverse()
