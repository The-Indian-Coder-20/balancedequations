from input import reactants, products

reactantsCount, productsCount = [], []

while len(reactants) != 0:
    for i in range(len(reactants)):
        if reactants[i] not in reactantsCount:
            reactantsCount.append([reactants[i], reactants[i + 1]])
            reactants.replace(i, "")
            reactants.replace(i + 1, "")
        pass
print(reactantsCount)