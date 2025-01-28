from input import finalReactantsCount, finalProductsCount

tempReactantList = []

#Duplicate checker only made to handle up to two duplicates in one compound e.g. C1H3C1O1O1H1

for i in finalReactantsCount:
    for j in range(len(i)):
        if i.count(i[j]) <= 2 and i[j] not in tempReactantList:
            tempReactantList.append(i[j])
            tempReactantList.append(i[j + 1])
        elif i[j] in tempReactantList and type(i[j]) != int:
            tempReactantList[tempReactantList.index(i[j]) + 1] += i[j + 1]
        elif type(i[j]) == str:
            tempReactantList.append(i[j])
            tempReactantList.append(i[j + 1])