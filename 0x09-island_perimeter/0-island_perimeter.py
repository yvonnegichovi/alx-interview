#!/usr/bin/python3
""" Interview task that creates an Island perimeter"""


def island_perimeter(grid):
    """ Returns a perimeter of the island described in grid
        Args:
            - grid: a list of the integers:
                - 0 represents water
                - 1 represents land
                - Each cell is square with a side length of 1
                - Cells are connected horizontally/vertically (not diagonally)
        returns:
            - perimeter of the island
    """
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1
    return perimeter
