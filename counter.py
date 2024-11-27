from input import reactantsCount, productsCount

reactantElements, productElements = [], []

for i in reactantsCount:
    if type(i) == str:
        reactantElements.append(i)
for i in productsCount:
    if type(i) == str:
        productElements.append(i)
print(reactantElements, productElements)