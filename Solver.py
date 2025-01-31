from sympy import Matrix, symbols
from counter import nonUsageMatrix, uniqueElementsList

matrix = Matrix(nonUsageMatrix)

rref_matrix = matrix.rref()

finalMatrixCounts = []

for j in range(len(rref_matrix[0])):
    print(rref_matrix[0][j])
    if rref_matrix[0][j] != 1 and rref_matrix[0][j] != 0:
        finalMatrixCounts.append(rref_matrix[0][j])

print(rref_matrix)
print(finalMatrixCounts)

t = symbols("t")

for i in range(len(finalMatrixCounts)):
    finalMatrixCounts[i] = finalMatrixCounts[i] * t

if len(nonUsageMatrix) - 1 <= len(uniqueElementsList) - 1:
    for i in range(((len(uniqueElementsList) - 1) - (len(nonUsageMatrix) - 1))):
        finalMatrixCounts.append(t)

print(finalMatrixCounts)