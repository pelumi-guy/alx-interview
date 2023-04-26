#!/usr/bin/python3
"""
0. Lockboxes
"""


# def add_list_to_set(_list, _set):
#     """
#     Adds values in a list to a set
#     """
#     for each in _list:
#         _set.add(each)


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes in a list of boxes can be opened.
    """
    opened_boxes = {0}
    keys = {*boxes[0]}

    opened_a_box = True
    while opened_a_box:
        opened_a_box = False
        for i, box in enumerate(boxes):
            if i in keys and i not in opened_boxes:
                # add_list_to_set(box, keys)
                for each in box:
                    keys.add(each)
                opened_boxes.add(i)
                # print('opened:', opened, end=' ')
                # print('keys:', keys)
                opened_a_box = True

    return len(opened_boxes) == len(boxes)
