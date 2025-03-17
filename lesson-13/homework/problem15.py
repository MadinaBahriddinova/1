import numpy as np

matrix_5x5 = np.random.rand(5, 5)

row_sums = np.sum(matrix_5x5, axis=1)  # Sum along columns (row-wise)
col_sums = np.sum(matrix_5x5, axis=0)  # Sum along rows (column-wise)

print("5x5 Matrix:\n", matrix_5x5)
print("Row-wise Sums:\n", row_sums)
print("Column-wise Sums:\n", col_sums)
