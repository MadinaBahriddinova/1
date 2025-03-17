import numpy as np

matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)

result_matrix = np.dot(matrix_5x3, matrix_3x2)

print("5x3 Matrix:\n", matrix_5x3)
print("3x2 Matrix:\n", matrix_3x2)
print("Resultant 5x2 Matrix:\n", result_matrix)
