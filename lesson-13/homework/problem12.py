import numpy as np

A = np.random.rand(3, 4)
B = np.random.rand(4, 3)

matrix_product = np.dot(A, B)

print("Matrix A (3x4):\n", A)
print("Matrix B (4x3):\n", B)
print("Matrix Product (A ⋅ B) (3x3):\n", matrix_product)
