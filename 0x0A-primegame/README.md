# 0x0A. Prime Game

## Description
This project involves solving a competitive game scenario using concepts from prime numbers, game theory, and algorithm optimization. The goal is to determine the winner of a game where players take turns removing prime numbers and their multiples from a set of consecutive integers.

### Problem Statement
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples. The player who cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

- **Prototype:** `def isWinner(x, nums)`
  - `x`: The number of rounds.
  - `nums`: An array of integers where each element represents the value of `n` for a round.
- **Return:** The name of the player that won the most rounds. If the winner cannot be determined, return `None`.

### Example
Given `x = 3` and `nums = [4, 5, 1]`:

1. **First round** (n=4):
   - Maria picks 2 and removes 2, 4, leaving 1, 3.
   - Ben picks 3 and removes 3, leaving 1.
   - Ben wins because there are no prime numbers left for Maria to choose.
  
2. **Second round** (n=5):
   - Maria picks 2 and removes 2, 4, leaving 1, 3, 5.
   - Ben picks 3 and removes 3, leaving 1, 5.
   - Maria picks 5 and removes 5, leaving 1.
   - Maria wins because there are no prime numbers left for Ben to choose.
  
3. **Third round** (n=1):
   - Ben wins because there are no prime numbers for Maria to choose.

**Result:** Ben has the most wins.

### Key Concepts
To solve the problem, you will need a good understanding of the following concepts:

- **Prime Numbers:** Understanding prime numbers and how to efficiently identify them within a range.
- **Sieve of Eratosthenes:** An efficient algorithm to find all prime numbers up to any given limit.
- **Game Theory:** Basic principles of competitive games, optimal play, and strategic decision-making.
- **Dynamic Programming/Memoization:** Techniques to optimize solutions for multiple rounds by reusing previous results.
- **Python Programming:** Implementation using loops, conditionals, arrays, and lists to manage the game state.

### Requirements
- **Editor:** vi, vim, emacs
- **Python Version:** Python 3.4.3 on Ubuntu 20.04 LTS
- **Code Style:** PEP 8 (version 1.7.x)
- **Executable:** All files must be executable
- **Mandatory Files:** `README.md` file at the root of the project folder

### Example Usage
```bash
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
carrie@ubuntu:~/0x0A-primegame$
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben