from input import reactantsCount, productsCount

print(reactantsCount, productsCount)

uniqueElementsList = []

for i in reactantsCount:
    if i not in uniqueElementsList and i not in "123456789":
        uniqueElementsList.append(i)
for i in productsCount:
    if i not in uniqueElementsList and i not in "123456789":
        uniqueElementsList.append(i)

