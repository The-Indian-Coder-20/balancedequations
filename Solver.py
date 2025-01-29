from counter import nonUsageMatrix
from sympy import Matrix

matrix = Matrix(nonUsageMatrix)

rref_matrix = matrix.rref()

finalMatrixCounts = []

for j in range(len(rref_matrix[0])):
    if rref_matrix[0][j] < 0:
        finalMatrixCounts.append(rref_matrix[0][j])
