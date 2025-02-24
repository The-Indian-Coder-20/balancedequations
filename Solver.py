from sympy import Matrix
from counter import nonUsageMatrix, finalCounts, totalPrRe, reactantsList, productsList
from fractions import Fraction as fr
import math
import functools

matrix = Matrix(nonUsageMatrix)

rref_matrix = matrix.rref()

finalMatrixCounts = []

for j in range(len(rref_matrix[0])):
    if rref_matrix[0][j] != 1 and rref_matrix[0][j] != 0:
        finalMatrixCounts.append(rref_matrix[0][j])

denominatorList = []

for i in range(len(finalMatrixCounts)):
    denominator = fr(finalMatrixCounts[i]).limit_denominator().denominator
    if denominator not in denominatorList and finalMatrixCounts[i] != 1:
        denominatorList.append(denominator)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_numbers(*numbers):
    return functools.reduce(lcm, numbers)

finalDenominator = lcm_of_numbers(*denominatorList)

if len(finalMatrixCounts) != len(finalCounts):
    for i in range((len(finalCounts)) - (len(finalMatrixCounts))):
        finalMatrixCounts.append(1)

for i in range(len(finalMatrixCounts)):
    if finalMatrixCounts[i] != 1:
        finalMatrixCounts[i] = int(finalMatrixCounts[i] * (-1 * finalDenominator))
    else:
        finalMatrixCounts[i] = int(finalMatrixCounts[i] * finalDenominator)

for i in range(len(finalMatrixCounts)):
    if finalMatrixCounts[i] != 1:
        totalPrRe[i] = f"{finalMatrixCounts[i]}({totalPrRe[i]})"

finalReactantsList, finalProductsList = [], []

for i in range(len(reactantsList)):
    finalReactantsList.append(f"{totalPrRe[i]}")
for i in range(len(productsList)):
    finalProductsList.append(f"{totalPrRe[i + len(reactantsList)]}")

for index in range(len(finalReactantsList)):
    if index != len(finalReactantsList) - 1:
        finalReactantsList[index] = f"{finalReactantsList[index]} + "
for index in range(len(finalProductsList)):
    if index != len(finalProductsList) - 1:
        finalProductsList[index] = f"{finalProductsList[index]} + "

reactants, products = "", ""

for i in finalReactantsList:
    reactants += i
for i in finalProductsList:
    products += i

print(f"""
The balanced chemical equation is:

{reactants} => {products}""")