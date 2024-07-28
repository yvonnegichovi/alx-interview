# 0x08. Making Change

## Algorithm | Python

### Project Overview

This project involves solving a classic problem in the realm of dynamic programming and greedy algorithms: the coin change problem. The objective is to determine the minimum number of coins required to make up a given total amount, using a list of coin denominations. This exercise is designed to enhance your understanding of algorithms and their efficiency.

### Key Concepts

#### Greedy Algorithms
- Understanding how greedy algorithms work and their application to the coin change problem.
- Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.

#### Dynamic Programming
- Basic principles of dynamic programming as a method to solve optimization problems.
- The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.

#### Algorithmic Complexity
- Analyzing the time and space complexity of algorithms.
- Striving for solutions with lower complexity to meet runtime constraints.

#### Problem-Solving Strategies
- Breaking down the problem into smaller, manageable sub-problems.
- Iterative vs. recursive approaches to dynamic programming.

#### Python Programming
- Manipulating lists and using list comprehensions.
- Implementing functions with efficient looping and conditional statements.

### Resources

- **Python Official Documentation:**
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)
- **GeeksforGeeks Articles:**
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials:**
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=1R0_7HqNaW0) for a visual and step-by-step explanation of the dynamic programming approach.

### Requirements

- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A `README.md` file at the root of the folder of the project is mandatory
  - Your code should use the PEP 8 style (version 1.7.x)
  - All your files must be executable

### Tasks

#### 0. Change comes from within
- **Mandatory**
- **Score: 0.0% (Checks completed: 0.0%)**
- **Task:** Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
- **Prototype:** `def makeChange(coins, total)`
- **Return:** fewest number of coins needed to meet total
  - If total is 0 or less, return 0
  - If total cannot be met by any number of coins you have, return -1
  - `coins` is a list of the values of the coins in your possession
  - The value of a coin will always be an integer greater than 0
  - You can assume you have an infinite number of each denomination of coin in the list
- **Note:** Your solution’s runtime will be evaluated in this task

```python
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$

### Repository

- **GitHub repository:** `alx-interview`
- **Directory:** `0x08-making_change`
- **File:** `0-making_change.py`
```

This `README.md` file includes all the necessary information about the project, including an overview, key concepts, resources, requirements, task descriptions, and sample usage.
