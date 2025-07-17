import numpy as np

# Coefficent matrix A
A = np.array([
    [2, 3],
    [-1, 4]
])

# Varialbles vector X
X = np.array([
    [2],
    [1]
])

# Constant vector B
B = np.array([
    [8],
    [2]
])

# Matrix multiplication
AX = A @ X

# Ouput
print("A =\n", A)
print("X =\n", X)
print("B =\n", B)
print("A @ B =\n", AX)

# Verification
print("Does 1 @ X equal B? -> ", np.allclose(AX, B))

# Bonus: solve the system
solution = np.linalg.solve(A, B)
print("\nSolved (x, y) using numpy.linalg.solve:\n", solution)