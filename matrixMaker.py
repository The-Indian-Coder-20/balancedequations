import numpy as np
from counter import uniqueElementsList, finalProductsCount, finalReactantsCount, uniqueElementsCountList
from input import reactantsList, productsList

elementMatrix = []

print(uniqueElementsCountList, uniqueElementsList, reactantsList, productsList)

for i in range(len(uniqueElementsList)):
    elementMatrix.append([])
    for j in range(len(reactantsList)):
        if uniqueElementsList[i] in reactantsList[j]:
            if len(uniqueElementsList[i]) == 1:
                elementMatrix[i].append(int(reactantsList[j][reactantsList[j].index(uniqueElementsList[i]) + 1]))
            else:
                elementMatrix[i].append(int(reactantsList[j][reactantsList[j].index(uniqueElementsList[i]) + 2]))
        else:
            elementMatrix[i].append(0)
print(elementMatrix)