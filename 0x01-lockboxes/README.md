# 0x01. Lockboxes

## Overview
This project involves developing a Python solution to determine if all lockboxes in a sequence can be opened given a list of keys within each box. The goal is to apply algorithmic techniques and Python programming skills to solve the problem efficiently.

## Learning Objectives
To complete this project, you will need to understand and utilize the following concepts:
- **Lists and List Manipulation**
  - Accessing elements, iterating, and modifying lists dynamically.
  - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)
- **Graph Theory Basics**
  - Concepts related to traversal algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS).
  - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)
- **Algorithmic Complexity**
  - Understanding time and space complexity for efficient algorithms.
  - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)
- **Recursion**
  - Implementing recursive solutions for traversing keys and boxes.
  - [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)
- **Queue and Stack**
  - Using queues and stacks for BFS and DFS implementations.
  - [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-in-python/)
- **Set Operations**
  - Using sets to track visited boxes and available keys.
  - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Requirements
- **Editors:** `vi`, `vim`, `emacs`
- **OS:** Ubuntu 20.04 LTS
- **Python Version:** Python 3.4.3
- **PEP 8 Style:** Version 1.7.x
- **File Execution:** All files must be executable
- **Shebang:** First line of all files should be `#!/usr/bin/python3`
- **Documentation:** Your code should be well-documented

## Task
### 0. Lockboxes
Write a method `canUnlockAll(boxes)` that determines if all the boxes can be opened.

**Prototype:**
```python
def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
All keys are positive integers
There may be keys without corresponding boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, otherwise return False
Example Usage:

python
Copy code
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
