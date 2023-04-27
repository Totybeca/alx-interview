#!/usr/bin/python3

def can_unlock_all(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes.

    Returns:
        True if all the boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)  # Number of boxes in the list
    box_dict = {}  # Dictionary containing the boxes that can be opened
    index = 0  # Index of the current box being checked

    for box in boxes:  # Iterate over each box in the list
        if not isinstance(box, list):
            raise ValueError("Input must be a list of lists.")
        
        if len(box) == 0 or index == 0:
            box_dict[index] = -1

        for key in box:
            if key < num_boxes and key != index:
                box_dict[key] = key

        if len(box_dict) == num_boxes:
            return True  # All boxes can be opened

        index += 1

    return False  # Not all boxes can be opened

