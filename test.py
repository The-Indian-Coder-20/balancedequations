from sympy import Matrix

finalMatrixCounts = []

rref_matrix = (Matrix([
[1, 0, 0, 0, 0, -1/12],
[0, 1, 0, 0, 0,    -1],
[0, 0, 1, 0, 0,  -7/4],
[0, 0, 0, 1, 0, -1/12],
[0, 0, 0, 0, 1,  -7/4]]), (0, 1, 2, 3, 4))



print(finalMatrixCounts)