from input import reactantsCount, productsCount, reactantsList, productsList

uniqueElementsList = []
uniqueElementsCountList = []

finalReactantsCount, finalProductsCount = [], []
tempList = []

#Integer converter for reactants
for i in range(len(reactantsCount)):
    if reactantsCount[i] in "123456789":
        reactantsCount[i] = int(reactantsCount[i])
#Integer converter for products
for i in range(len(productsCount)):
    if productsCount[i] in "123456789":
        productsCount[i] = int(productsCount[i])

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
        finalReactantsCount[tempPosition] += productsCount[i]
    
#Appends unique elements to the list from the reactantsCount list
for i in finalReactantsCount:
    if i not in uniqueElementsList and type(i) != int:
        uniqueElementsList.append(i)

#Appends the # of atoms for the unique elements to the list
for i in finalReactantsCount:
    if type(i) == int:
        uniqueElementsCountList.append(i)

finalReactantsList, finalProductsList = [], []

#Parentheses multiplier for reactantsList
tempWord = ""
tempNum = ""
reactant = ""
for i in range(len(reactantsList)):
    j = 0
    while j <= len(reactantsList[i]) - 1:
        if reactantsList[i][j].isalpha():
            if len(tempNum) != 0:
                reactant += tempNum
                tempNum = ""
            tempWord += reactantsList[i][j]
        elif reactantsList[i][j] in "123456789":
            reactant += tempWord
            if j == len(reactantsList[i]) - 1:
                if len(tempNum) != 0:
                    reactant += tempNum + reactantsList[i][j]
                else:
                    reactant += reactantsList[i][j]
            else:
                tempNum += reactantsList[i][j]
            tempWord = ""
        elif reactantsList[i][j] == "(":
            if len(tempNum) != 0:
                reactant += tempNum
            if len(tempWord) != 0:
                reactant += tempWord
            tempReactant = reactantsList[i][j + 1:reactantsList[i].index(")") + 2]
            tempTempWord, tempTempNum = "", ""
            for x in range(len(tempReactant)):
                if tempReactant[x].isalpha():
                    if len(tempTempNum) != 0:
                        print(tempReactant)
                        reactant += str(int(tempTempNum)*int(tempReactant[tempReactant.index(")") + 1]))
                        tempTempNum = ""
                    tempTempWord += tempReactant[x]
                elif tempReactant[x] in "123456789":
                    if x == tempReactant.index(")") - 1:
                        reactant += 
                    tempTempNum += tempReactant[x]
                    reactant += tempTempWord
                    tempTempWord = ""
                elif tempReactant[x] == ")":
                    break
            j = reactantsList[i].index(")") + 1
        j += 1
    print(reactant)
    finalReactantsList.append(reactant)
    tempTempWord, tempTempNum = "", ""
    tempWord, tempNum = "", ""
    reactant = ""
