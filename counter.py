from input import finalReactantsCount, finalProductsCount, reactantsList, productsList, productsCount, reactantsCount

uniqueElementsList = []
for i in reactantsCount:
    if i not in uniqueElementsList and i.isalpha():
        uniqueElementsList.append(i)
for i in productsCount:
    if i not in uniqueElementsList and i.isalpha():
        uniqueElementsList.append(i)

reactantsVectorsList, productsVectorsList = [], []

for i in reactantsList:
    reactantsVectorsList.append([])
for i in productsList:
    productsVectorsList.append([])

for i in uniqueElementsList:
    for j in range(len(reactantsList)):
        if i in reactantsList[j]:
            reactantsVectorsList[j].append(finalReactantsCount[j][finalReactantsCount[j].index(i) + 1])

for i in uniqueElementsList:
    for j in range(len(productsList)):
        if i in productsList[j]:
            productsVectorsList[j].append(finalProductsCount[j][finalProductsCount[j].index(i) + 1])

print(reactantsVectorsList, productsVectorsList)
