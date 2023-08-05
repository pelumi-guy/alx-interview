#!/usr/bin/python3
"""
0x05. N Queens
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

cols = set()
posDiag = set()  # row + col
negDiag = set()  # row - col

res = []
solutions = []


def backtrack(row):
    """
    Bactracking helper function
    """
    global res
    if row == n:
        # print(res)
        solutions.append(res.copy())
        return

    for col in range(n):
        if col in cols or (row + col) in posDiag or (row - col) in negDiag:
            continue

        cols.add(col)
        posDiag.add(row + col)
        negDiag.add(row - col)
        res.append([row, col])

        # On to next row to continue bruteforcing for a solution
        backtrack(row + 1)

        # Backtracking cleanup
        cols.remove(col)
        posDiag.remove(row + col)
        negDiag.remove(row - col)
        # if [row, col] in res:
        res.remove([row, col])


backtrack(0)

for solution in solutions:
    print(solution)
