from validElementChecker import reactantsCount, productsCount

uniqueElementsList = []
uniqueElementsCountList = []

finalReactantsCount, finalProductsCount = [], []
tempList = []

#Integer converter for reactants
for i in range(len(reactantsCount)):
    if reactantsCount[i] in "123456789":
        reactantsCount[i] = int(reactantsCount[i])
#Integer converter for products
for i in range(len(reactantsCount)):
    if reactantsCount[i] in "123456789":
        reactantsCount[i] = int(reactantsCount[i])

#Duplicate checker for reactants
for i in range(len(reactantsCount)):
    if reactantsCount[i] not in finalReactantsCount and type(reactantsCount[i]) != int:
        finalReactantsCount.append(reactantsCount[i])
        finalReactantsCount.append(0)
    elif type(reactantsCount[i]) == int:
        tempPosition = finalReactantsCount.index(reactantsCount[i-1]) + 1
        finalReactantsCount[tempPosition] += reactantsCount[i]
#Duplicate checker for products
for i in range(len(productsCount)):
    if productsCount[i] not in finalProductsCount and type(productsCount[i]) != int:
        finalProductsCount.append(productsCount[i])
        finalProductsCount.append(0)
    elif type(productsCount[i]) == int:
        tempPosition = finalProductsCount.index(productsCount[i-1]) + 1
        finalReactantsCount[tempPosition] += reactantsCount[i]
    
#Appends unique elements to the list from the reactantsCount list
for i in finalReactantsCount:
    if i not in uniqueElementsList and type(i) != int:
        uniqueElementsList.append(i)

#Appends the # of atoms for the unique elements to the list
for i in finalReactantsCount:
    if type(i) == int:
        uniqueElementsCountList.append(i)

print(uniqueElementsList)
print(uniqueElementsCountList)