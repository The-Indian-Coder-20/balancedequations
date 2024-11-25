from input import reactants, products

reactantsCount, productsCount = [], []
tempWord = ""

for i in range(len(reactants)):
    if reactants[i].isalpha():
        tempWord += reactants[i]
    elif reactants[i] in "123456789":
        if reactants[i-1] in reactantsCount:
            reactantsCount[reactantsCount.index(reactants[i-1]) + 1] += int(reactants[i])
            tempWord = ""
        else:
            reactantsCount.append(tempWord)
            reactantsCount.append(int(reactants[i]))
            tempWord = ""

for i in range(len(products)):
    if products[i].isalpha():
        tempWord += products[i]
    elif products[i] in "123456789":
        if products[i-1] in productsCount:
            productsCount[productsCount.index(products[i-1]) + 1] += int(products[i])
            tempWord = ""
        else:
            productsCount.append(tempWord)
            productsCount.append(int(products[i]))
            tempWord = ""

print(reactantsCount, productsCount)

reactantElements, productElements = [], []
for i in reactantsCount:
    if type(i) == str:
        reactantElements.append(i)
for i in productsCount:
    if type(i) == str:
        productElements.append(i)
print(reactantElements, productElements)