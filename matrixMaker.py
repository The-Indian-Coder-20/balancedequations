import numpy as np
from counter import uniqueElementsList, finalProductsCount, finalReactantsCount, uniqueElementsCountList
from input import reactantsList, productsList

elementMatrix = []

for i in range(len(uniqueElementsList)):
    elementMatrix.append([])
    for j in range(len(reactantsList)):
        if uniqueElementsList[i] in reactantsList[j]:
            elementMatrix[i].append(reactantsList[j])
print(elementMatrix)