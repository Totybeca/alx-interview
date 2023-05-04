#!/usr/bin/python3

"""
    This method determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        The function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: The number of characters to be displayed
        return: The number of min operations
    """

    begin = 1
    num = 0
    count = 0
    while begin < n:
        remainder = n - begin
        if (remainder % begin == 0):
            num = begin
            begin += num
            count += 2
        else:
            begin += num
            count += 1
    return count