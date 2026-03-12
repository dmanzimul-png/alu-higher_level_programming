# ALU Python More Data Structures - Task 0

## Task 0: Squared simple

This task implements a function `square_matrix_simple(matrix=[])` that:

- Takes a 2D matrix (list of lists) of integers
- Returns a **new matrix** of the same size
- Each element is the square of the corresponding element in the input
- The original matrix is **not modified**
- No external modules are used

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)  # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
