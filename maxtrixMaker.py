import numpy as np
from counter import reactantsCount, productsCount, reactantElements, productElements

elementsMatrix = []
for x in range(len(reactantElements)):
    elementsMatrix.append([])

print(reactantsCount, productsCount, reactantElements, productElements)
print(elementsMatrix)

for j in range(len(reactantElements)):
    for i in range(len(reactantsCount)):
        if type(reactantsCount[i]) == int:
            if reactantElements[j] in reactantsCount[i-1]:
                elementsMatrix[j].append(reactantsCount[i])