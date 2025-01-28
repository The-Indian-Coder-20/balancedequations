from counter import nonUsageMatrix
from sympy import Matrix

print(nonUsageMatrix)

matrix = Matrix(nonUsageMatrix)

print(matrix)

rref_matrix, pivot_columns = matrix.rref()