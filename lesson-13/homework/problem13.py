import numpy as np

matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)

matrix_vector_product = np.dot(matrix_3x3, vector_3x1)

print("3x3 Matrix:\n", matrix_3x3)
print("3x1 Column Vector:\n", vector_3x1)
print("Matrix-Vector Product:\n", matrix_vector_product)
