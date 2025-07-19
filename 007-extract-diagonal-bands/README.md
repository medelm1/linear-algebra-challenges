# Challenge 007: Extract Diagonal Bands

## Challenge Statement

Write a function that takes a **2D square NumPy array** and returns a **1D array** that contains all elements from the **main diagonal and the diagonals immediately above and below it** (the 3 central diagonals).

That is:

- The main diagonal: where row index = column index.
- The upper diagonal: just above the main (row index = column index - 1).
- The lower diagonal: just below the main (row index = column index + 1).

## Requirements

- Use NumPy functions like np.diagonal or slicing.
- Do not use loops (`for`, `while`).
- Assume input is a square 2D NumPy array.

## Function Signature
```python
import numpy as np

def extract_diagonal_band(arr: np.ndarray) -> np.ndarray:
    pass
```