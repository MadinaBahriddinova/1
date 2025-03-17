import numpy as np

matrix_5x5 = np.random.rand(5, 5)
normalized_matrix = (matrix_5x5 - np.min(matrix_5x5)) / (np.max(matrix_5x5) - np.min(matrix_5x5))

print("Original 5x5 Matrix:\n", matrix_5x5)
print("Normalized 5x5 Matrix:\n", normalized_matrix)
