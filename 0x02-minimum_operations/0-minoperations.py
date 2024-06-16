#!/usr/bin/python3
"""
This module works on minimum operations
"""


def minOperations(n):
    """
    This method calculates the fewest number of operations needed to result in
    exactly n H characters in the file
    The text editor can execute only two operations in this file:
        - Copy All
        - Paste
    Returns an integer
    """
    if not n:
        return 0
