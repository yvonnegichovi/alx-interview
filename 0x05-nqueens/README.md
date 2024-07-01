# 0x05. N Queens

## Algorithm
The N Queens problem is a classic algorithmic challenge in computer science and mathematics. The objective is to place N non-attacking queens on an N×N chessboard using the backtracking algorithm.

## Python

**Project Details:**
- **Weight:** 1
- **Project Duration:** Jul 1, 2024 6:00 AM to Jul 5, 2024 6:00 AM
- **Checker Release:** Jul 2, 2024 6:00 AM
- **Auto Review:** Launched at the deadline

## Concepts Needed:

### Backtracking Algorithms:
- **Understanding:** Explore all potential solutions and backtrack when a solution cannot be completed.
- **Resources:**
  - [Backtracking Introduction](#)

### Recursion:
- **Using Recursive Functions:** Implement backtracking algorithms.
- **Resources:**
  - [Recursion in Python](#)

### List Manipulations in Python:
- **Creating and Manipulating Lists:** Store the positions of queens on the board.
- **Resources:**
  - [Python Lists](#)

### Python Command Line Arguments:
- **Handling Command-Line Arguments:** Utilize the `sys` module.
- **Resources:**
  - [Command Line Arguments in Python](#)

By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N Queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

## Additional Resources
- [Mock Interview](#)

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code should use the PEP 8 style (version 1.7.*)
- All files must be executable

## Tasks

### 0. N Queens (Mandatory)
![Judit Polgár](https://upload.wikimedia.org/wikipedia/commons/7/7f/Judit_Polg%C3%A1r_Chess.jpg)

The N Queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

**Usage:** `nqueens N`

- If the user calls the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- `N` must be an integer greater or equal to `4`
  - If `N` is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
  - If `N` is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem, one solution per line
  - Format: see example
  - Solutions do not need to be printed in a specific order
- Only the `sys` module is allowed

**Example:**
```shell
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
