sizes = len(boxes)  # The sizes of the list of boxes.
    box = {}  # The dictionary that will contain the boxes to  be opened.
    a = 0  #  the box that will be checked.


for keys in boxes:  # for each of the boxes in the list of boxes.
    if len(keys) == 0 or a == 0:
        box[a] = -1
    for key in keys:
        if key < sizes and key != a:
            box[key] = key  # add box to dictionary.
    if len(box) == sizes:
        return True  # all the boxes can now  be opened.
    a += 1
return False
