#!/usr/bin/python3
"""This is the solutions to lockboxes"""


def canUnlockAll(boxes):
    """This function receives a list of lists and checks if all
    boxes contains keys to open all boxes
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    keys = boxes[0]
    while keys:
        new_keys = set()
        for key in keys:
            if not unlocked[key]:
                unlocked[key] = True
                new_keys.update(boxes[key])
        keys = new_keys

    return all(unlocked)
