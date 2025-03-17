import numpy as np

# Task 3: Solve system of equations
a = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b = np.array([7, 4, 5])
x = np.linalg.solve(a, b)

print("Solution (x, y, z):", x)