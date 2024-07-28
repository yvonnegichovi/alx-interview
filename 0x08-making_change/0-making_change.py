#!/usr/bin/python3
""" This moduke handles greedy algorithm to handle making change task"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to a given amount total
    Return: fewest number of coins needed to meet total"""
    if total is 0:
        return 0
