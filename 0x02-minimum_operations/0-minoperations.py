#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):

    if n <= 1:
        return 0
    number, division, number-Of_Operations = n, 2, 0
    while number > 1:
        if number % division == 0:
            number = number / division
            num-Of_Operations = num-Of_Operations + division
        else:
            division += 1
    return number-Of_Operations