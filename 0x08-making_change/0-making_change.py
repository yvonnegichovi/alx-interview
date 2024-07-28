#!/usr/bin/python3
""" This moduke handles greedy algorithm to handle making change task"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to a given amount total
    Args:
        - coins: a list of the values of coins in your possession
        - total: a given amount
    Return: fewest number of coins needed to meet total"""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
