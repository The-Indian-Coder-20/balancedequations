import numpy as np
from counter import uniqueElementsList
from input import reactantsCount, reactantsList, productsCount, productsList

print(reactantsCount, productsCount)
elementMatrix = []

for i in range(len(uniqueElementsList)):
    elementMatrix.append([])

for i in range(len(uniqueElementsList)):
    for j in range(len(reactantsList)):
        if uniqueElementsList[i] in reactantsList[j] and len(uniqueElementsList) == 1:
            print("yes")
            elementMatrix[i].append(reactantsCount[reactantsCount.index(elementMatrix[i]) + 1])
        elif uniqueElementsList[i] in reactantsList[j] and len(uniqueElementsList) == 2:
            print("no")
            elementMatrix[i].append(reactantsCount[reactantsCount.index(elementMatrix[i]) + 1])
        else:
            elementMatrix[i].append("0")

print(elementMatrix)