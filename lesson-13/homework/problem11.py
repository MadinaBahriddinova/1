import numpy as np

matrix_3x3 = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3)

print("3x3 Matrix:\n", matrix_3x3)
print("Determinant:", determinant)
