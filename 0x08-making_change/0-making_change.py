#!/usr/bin/python3
""" This moduke handles greedy algorithm to handle making change task"""


def makeChange(coins, total):
    """ Determines the fewest number of coins needed to a given amount total
    Args:
        - coins: a list of the values of coins in your possession
        - total: a given amount
    Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    coins.sort(reverse=True)
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1

