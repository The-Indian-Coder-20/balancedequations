from input import finalReactantsCount, finalProductsCount, reactantsList, productsList

uniqueElementsList = []

for i in range(len(finalReactantsCount)):
    for j in finalReactantsCount[i]:
        if j not in uniqueElementsList and type(j) == str:
            uniqueElementsList.append(j)

print(uniqueElementsList)

reactantsVectorsList, productsVectorsList = [], []

for i in reactantsList:
    reactantsVectorsList.append([])
for i in productsList:
    productsVectorsList.append([])

for i in uniqueElementsList:
    for j in range(len(reactantsList)):
        if i in reactantsList[j]:
            reactantsVectorsList[j].append(finalReactantsCount[j][finalReactantsCount[j].index(i) + 1])
        else:
            reactantsVectorsList[j].append(0)

for i in uniqueElementsList:
    for j in range(len(productsList)):
        if i in productsList[j]:
            productsVectorsList[j].append(finalProductsCount[j][finalProductsCount[j].index(i) + 1])
        else:
            productsVectorsList[j].append(0)

print(uniqueElementsList, reactantsVectorsList, productsVectorsList)
