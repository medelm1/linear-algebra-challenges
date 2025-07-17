# Challenge 001 — Matrix Playground: Representing a System of Equations

# 📌 Problem Statement

You're given a simple system of linear equations:

```
2x + 3y = 8
-1x + 4y = 2
```

Your task is to:

1. Represent this system as:
   - A **coefficient matrix** `A`
   - A **variable vector** `X`
   - A **constant vector** `B`

2. Perform matrix multiplication to verify the matrix equation:
```
A · X = B
```

3. Print all matrices and the result of the multiplication.

---

## Goals

- Understand matrix representation of linear systems
- Practice creating and manipulating NumPy arrays
- Learn matrix multiplication using the `@` operator

---

## Example Output

```
A =
[[ 2 3]
[-1 4]]

X =
[[2]
[1]]

B =
[[8]
[2]]

A @ X =
[[8]
[2]]

Does A @ X equal B? -> True
```

---

## Optional Bonus

- Solve the system using `numpy.linalg.solve(A, B)`
- Print the solution for `x` and `y`

---

## References

- NumPy Array Basics: https://numpy.org/doc/stable/user/quickstart.html
- Matrix Multiplication: https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
