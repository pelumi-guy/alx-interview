#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev = triangle[i - 1]
        for idx, each in enumerate(prev):
            if idx < len(prev) - 1:
                row.append(each + prev[idx + 1])
        row.append(1)
        triangle.append(row)
    return triangle
