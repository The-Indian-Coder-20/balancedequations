from input import reactantsList, productsList
from duplicatechecker import finalReactantsCount, finalProductsCount

uniqueElementsList = []

for i in range(len(finalReactantsCount)):
    for j in finalReactantsCount[i]:
        if j not in uniqueElementsList and type(j) == str:
            uniqueElementsList.append(j)

totalReactants = []

for i in reactantsList:
    totalReactants.append(i)
for i in productsList:
    totalReactants.append(i)

finalCounts = []

for i in finalReactantsCount:
    finalCounts.append(i)
for i in finalProductsCount:
    finalCounts.append(i)

nonUsageMatrix = []

for element in uniqueElementsList:
    nonUsageMatrix.append([])

for i in range(len(finalCounts)):
    for element in uniqueElementsList:
        if element not in finalCounts[i]:
            nonUsageMatrix[uniqueElementsList.index(element)].append(0)
        else:
            for j in range(len(finalCounts[i])):
                if finalCounts[i][j] == element:
                    if i <= len(finalReactantsCount) - 1:
                        nonUsageMatrix[uniqueElementsList.index(element)].append(finalCounts[i][j + 1])
                    else:
                        nonUsageMatrix[uniqueElementsList.index(element)].append(int("-" + str(finalCounts[i][j + 1])))