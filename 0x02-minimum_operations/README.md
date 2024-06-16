# 0x02. Minimum Operations

## Project Overview

In this project, the goal is to calculate the minimum number of operations required to generate exactly `n` characters of `H` in a text file using only two operations: "Copy All" and "Paste". This involves understanding and implementing efficient algorithms, particularly using concepts from dynamic programming, prime factorization, and greedy algorithms.

## Key Concepts

### Dynamic Programming
Dynamic programming is a method used to solve problems by breaking them down into simpler subproblems and building up the solution step by step.

### Prime Factorization
Prime factorization involves breaking down a number into its prime factors. This is crucial for this problem as it can be reduced to finding the sum of the prime factors of the target number `n`.

### Code Optimization
Optimizing code is important for improving performance and efficiency. This involves using the best algorithms and data structures to achieve the desired outcome.

### Greedy Algorithms
Greedy algorithms involve making the best possible choice at each step with the hope of finding the global optimum.

### Basic Python Programming
Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.

## Requirements
- The project must be implemented in Python 3.4.3 on Ubuntu 20.04 LTS.
- The code should follow PEP 8 style guidelines.
- A `README.md` file is mandatory.
- All files must be executable.

## Example

For `n = 9`, the sequence of operations would be:
```
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```
Number of operations: 6

## Implementation

The function `minOperations` takes an integer `n` and returns the minimum number of operations required to get exactly `n` characters of `H`. If it is impossible to achieve, it returns 0.

## Repository Structure

```
.
├── 0-main.py
├── 0-minoperations.py
└── README.md
```

## `README.md` File

```markdown
# Minimum Operations

## Overview

This project aims to find the minimum number of operations required to generate exactly `n` characters of `H` using only "Copy All" and "Paste" operations.

## Key Concepts

- **Dynamic Programming**: Used to break down the problem into simpler subproblems.
- **Prime Factorization**: Essential for reducing the problem to finding the sum of prime factors.
- **Code Optimization**: Important for achieving efficient solutions.
- **Greedy Algorithms**: Useful for making optimal choices at each step.
- **Basic Python Programming**: Necessary for implementation.

## Requirements

- Python 3.4.3 on Ubuntu 20.04 LTS
- PEP 8 style guidelines
- Mandatory `README.md` file
- Executable files

## Example

For `n = 9`, the sequence of operations would be:
```
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```
Number of operations: 6

## Implementation

The `minOperations` function calculates the minimum number of operations needed to get exactly `n` characters of `H`. If it is impossible, it returns 0.

## Repository Structure

```
.
├── 0-main.py
├── 0-minoperations.py
└── README.md
```
```

## `0-main.py`

```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
```
