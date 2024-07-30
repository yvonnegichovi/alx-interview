# Island Perimeter

## Description

The Island Perimeter project involves calculating the perimeter of a single island in a 2D grid. The grid is represented by a list of lists of integers where:
- `0` represents water
- `1` represents land

The island is surrounded by water and does not contain any internal lakes.

## Requirements

- Python 3.4.3
- No external modules are allowed
- Code should follow PEP 8 style guidelines
- The grid is rectangular and its dimensions do not exceed 100x100

## Task

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the `grid`. 

### Function Signature

```python
def island_perimeter(grid: List[List[int]]) -> int:
    """
    Returns the perimeter of the island described in grid.

    :param grid: List of lists of integers representing the grid
    :return: Integer representing the perimeter of the island
    """
```

## Example

### Input

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

### Output

```
12
```

## Usage

To test the function, run the provided `0-main.py` script:

```bash
./0-main.py
```

This will execute the `island_perimeter` function with a sample grid and print the result.

## Author

Yvonne Ng'endo Gichovi

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can customize the author and license sections as needed. This README provides a clear overview of the project, its requirements, and how to use the function.
