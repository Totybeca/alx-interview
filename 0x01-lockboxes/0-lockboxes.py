#!/usr/bin/python3
"""This script will unlock the list of lists."""
"""Module that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """function takes a list of lists and the content
       of a list unlocks other lists.
    """

    keys = [0]
    for key in keys:
        for keyBox in boxes[key]:#for each box in the list of boxes.
            if keyBox not in keys and keyBox < len(boxes):
                keys.append(keyBox)
    if len(keys) == len(boxes):
        return True # all the boxes can be opened.
    return False

