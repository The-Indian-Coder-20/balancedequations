from input import finalReactantsCount, finalProductsCount

tempReactantList, tempProductList = [], []

#Duplicate checker only made to handle up to two duplicates in one compound e.g. C1H3C1O1O1H1

for i in finalReactantsCount:
    for j in range(len(i)):
        if i.count(i[j]) <= 2 and i[j] not in tempReactantList and type(i[j]) != int:
            tempReactantList.append(i[j])
            tempReactantList.append(i[j + 1])
        elif i[j] in tempReactantList and type(i[j]) != int:
            tempReactantList[tempReactantList.index(i[j]) + 1] += i[j + 1]
        elif type(i[j]) == str:
            tempReactantList.append(i[j])
            tempReactantList.append(i[j + 1])
    finalReactantsCount[finalReactantsCount.index(i)] = tempReactantList
    tempReactantList = []

for i in finalProductsCount:
    for j in range(len(i)):
        if i.count(i[j]) <= 2 and i[j] not in tempProductList and type(i[j]) != int:
            tempProductList.append(i[j])
            tempProductList.append(i[j + 1])
        elif i[j] in tempProductList and type(i[j]) != int:
            tempProductList[tempProductList.index(i[j]) + 1] += i[j + 1]
        elif type(i[j]) == str:
            tempProductList.append(i[j])
            tempProductList.append(i[j + 1])
    finalProductsCount[finalProductsCount.index(i)] = tempProductList
    tempProductList = []
