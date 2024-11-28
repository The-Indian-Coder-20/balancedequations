import numpy as np
from counter import uniqueElementsList
from input import finalReactantsCount, reactantsList, productsCount, finalProductsList

elementMatrix = []

for i in range(len(uniqueElementsList)):
    elementMatrix.append([])
    for j in range(len(reactantsList)):
        if uniqueElementsList[i] in reactantsList[j]:
            elementMatrix[i].append()

