from input import reactantsList, productsList, finalProductsCount, finalReactantsCount

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

for i in range(len(uniqueElementsList)):
    nonUsageMatrix.append([])
    for j in range(len(totalReactants)):
        if uniqueElementsList[i] in totalReactants[j]:
            if j <= len(reactantsList) - 1:
                nonUsageMatrix[i].append(finalCounts[j][finalCounts[j].index(uniqueElementsList[i]) + 1])
            else:
                nonUsageMatrix[i].append((finalCounts[j][finalCounts[j].index(uniqueElementsList[i]) + 1]) * -1)
        else:
            nonUsageMatrix[i].append(0)