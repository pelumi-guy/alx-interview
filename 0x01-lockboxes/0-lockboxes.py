#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes in a list of boxes can be opened.

    Args:
        boxes

    Return:
        True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        # print('current unlocked list:', unlocked, end=' ')
        # print('current n:', n)
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    return len(unlocked) == len(boxes)
