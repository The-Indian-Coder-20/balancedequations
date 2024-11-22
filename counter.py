from input import reactants, products

reactantsCount, productsCount = [], []
tempWord = ""
for i in range(len(reactants)):
    if reactants[i].isalpha():
        tempWord += reactants[i]
    elif reactants[i] in "123456789":
        if reactants[i-1] in reactantsCount:
            reactantsCount[reactants[i-1]] += reactants[i]
            tempWord = ""
        else:
            reactantsCount.append(tempWord)
            reactantsCount.append(reactants[i])
            tempWord = ""
print(reactantsCount)