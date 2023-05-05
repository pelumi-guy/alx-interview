#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    A method that calculates the fewest number of operations needed
    to result in exactly n H characters in a file.
    Using a text editor that can execute only two operations in this file:
    Copy All and Paste
    """
    if n <= 1:
        return 0

    pos = 1
    ops_counter = 0
    clipboard = 0
    while pos < n:
        if (n - pos) % pos == 0:
            clipboard = pos
            pos += clipboard
            ops_counter += 2
        else:
            pos += clipboard
            ops_counter += 1

    return ops_counter
