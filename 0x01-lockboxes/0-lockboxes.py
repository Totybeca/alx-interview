#!/usr/bin/python3
"""This script will unlock list of lists"""


def canUnlockAll(boxes):
    """This function takes the list of lists and the content
       of the list will unlock other lists.
    """
    keys = [0]
    for key in keys:
        for boxKeys in boxes[key]:
            if boxKeys not in keys and boxKeys < len(boxes):
                keys.append(boxKeys)
    if len(keys) == len(boxes):
        return True
    return False
