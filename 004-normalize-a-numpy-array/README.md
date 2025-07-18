# Challenge 004: Normalize a NumPy Array

## Challenge Statement
Write a function that takes a 1D NumPy array of numbers and returns a **normalized version** of that array, where the values are scaled to be between **0 and 1**, using **min-max normalization**:
```math
x_normalized = x - max(x) / max(x) - min(x)
```
If the input array contains **all identical values**, return an array of zeros of the same shape.

## Requirements
- Use NumPy only.
- Do not use explicit loops (`for`, `while`).
- Do not modify the original array.
- Handle division by zero if max equals min.

## Function Signature
```python
import numpy as np

def normalize_array(arr: np.ndarray) -> np.ndarray:
    pass
```