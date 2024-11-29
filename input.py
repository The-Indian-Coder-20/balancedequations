import re
import validElementChecker

reCount, prCount = 1, 1
reactantsCount, productsCount = [], []
tempWord = ""
valid_equation = re.compile(r'^[A-Za-z0-9()]+$')
mainKey = True
tempCount = 0
lastBracketIndex = 0
reactantsList, productsList = [], []

print("""If there is only one atom of the element, please input the number '1' after the element. (E.g. Na1).
""")

#Input parsing has been completed for regular chemical equations as well as those with parentheses.
while mainKey:

    key = True
    minorKey = True

    while key:
        while minorKey:
            reactant = input(f"What is reactant {reCount}? (...#): ")
            if reactant != "":
                reactantsList.append(reactant)
            i = 0
            if reactant != "":
                reCount += 1
                while i <= len(reactant) - 1 :
                    if reactant[i].isalpha():
                        tempWord += reactant[i]
                    elif reactant[i] in "123456789":
                        reactantsCount.append(tempWord)
                        tempReactantNum = reactant[i:]
                        tempNum = ""
                        for y in tempReactantNum:
                            if y in "123456789" and tempReactantNum.index(y) == len(tempReactantNum) - 1:
                                reactantsCount.append(y)
                                break
                            elif y in "123456789":
                                tempNum += y
                            else:
                                reactantsCount.append(tempNum)
                                i = reactant.index(y) - 1
                                break
                        tempWord = ""
                        tempNum = ""
                        tempReactantNum = ""
                    if i <= len(reactant) - 1:
                        if reactant[i] == "(":
                            tempWord = ""
                            tempReactant = reactant[i + 1:reactant.index(")") + 2]
                            for j in range(len(tempReactant)):
                                if tempReactant[j].isupper():
                                    reactantsCount.append(tempReactant[j])
                                    if tempReactant[j+1] not in "123456789" and not tempReactant[j+1].islower():
                                        reactantsCount.append(tempReactant[-1])
                                elif tempReactant[j].islower():
                                    tempPosition = reactantsCount[reactantsCount.index(tempReactant[j-1])]
                                    tempPosition += tempReactant[j]
                                    reactantsCount[reactantsCount.index(tempReactant[j-1])] = tempPosition
                                    if tempReactant[j+1] not in "123456789":
                                        reactantsCount.append(tempReactant[-1])
                                elif tempReactant[j] in "123456789" and j != len(tempReactant) - 1:
                                    reactantsCount.append(str(int(tempReactant[j])*int(tempReactant[tempReactant.index(")") + 1])))
                            tempWord = ""
                            i += (j + 1) 
                    i += 1
            else:
                minorKey = False
                if len(reactantsList) == 0:
                    print("No reactants entered. Please enter a reactant.")
                    minorKey = True
        if validElementChecker.isRealElementReactants(reactantsCount):
            print("All entered elements in reactants are valid.")
            key = False
        else:
            print("One or more entered elements in reactants are not valid.")
            key = True
            minorKey = True
            reactantsCount = []
            reactantsList = []
            reCount = 1

    key = True
    minorKey = True

    while key:
        while minorKey:
            product = input(f"What is product {prCount}? (...#): ")
            if product != "":
                productsList.append(product)
            i = 0
            if product != "":
                prCount += 1
                while i <= len(product) - 1 :
                    if product[i].isalpha():
                        tempWord += product[i]
                    elif product[i] in "123456789":
                        productsCount.append(tempWord)
                        tempProductNum = product[i:]
                        tempNum = ""
                        for y in tempProductNum:
                            if y in "123456789" and tempProductNum.index(y) == len(tempProductNum) - 1:
                                productsCount.append(y)
                                break
                            elif y in "123456789":
                                tempNum += y
                            else:
                                productsCount.append(tempNum)
                                i = product.index(y) - 1
                                break
                        tempWord = ""
                        tempNum = ""
                        tempProductNum = ""
                    if i <= len(product) - 1:
                        if product[i] == "(":
                            tempWord = ""
                            tempProduct = product[i + 1:product.index(")") + 2]
                            for j in range(len(tempProduct)):
                                if tempProduct[j].isupper():
                                    productsCount.append(tempProduct[j])
                                    if tempProduct[j+1] not in "123456789" and not tempProduct[j+1].islower():
                                        productsCount.append(tempProduct[-1])
                                elif tempProduct[j].islower():
                                    tempPosition = productsCount[productsCount.index(tempReactant[j-1])]
                                    tempPosition += tempProduct[j]
                                    productsCount[productsCount.index(tempProduct[j-1])] = tempPosition
                                    if tempProduct[j+1] not in "123456789":
                                        productsCount.append(tempProduct[-1])
                                elif tempProduct[j] in "123456789" and j != len(tempProduct) - 1:
                                    productsCount.append(str(int(tempProduct[j])*int(tempProduct[tempProduct.index(")") + 1])))
                            tempWord = ""
                            i += (j + 1) 
                    i += 1
            else:
                minorKey = False
                if len(productsList) == 0:
                    print("No products entered. Please enter a product.")
                    minorKey = True
        if validElementChecker.isRealElementProducts(productsCount):
            print("All entered elements in products are valid.")
            key = False
        else:
            print("One or more entered elements in products are not valid.")
            key = True
            minorKey = True
            productsCount = []
            productsList = []
            prCount = 1

    reactants, products = "", ""
    print(reactantsCount, productsCount)

    if all(valid_equation.fullmatch(item) for item in reactantsCount) and all(valid_equation.fullmatch(item) for item in productsCount):
        for i in reactantsList:
            if (reactantsList.index(i) != len(reactantsList) - 1):
                reactants += i + " + "
            else:
                reactants += i
        for i in productsList:
            if productsList.index(i) != len(productsList) - 1:
                products += i + " + "
            else:
                products += i
        print(f"The entered equation is {reactants} => {products}")
        check = input("Is the entered equation correct? [y/n] ")
        if check.lower() == "y":
            print("Proceeding...")
            mainKey = False
        else:
            print("Please re-enter the chemical equation")
            reactantsCount, productsCount = [], []
            reactantsList, productsList = [], []
            reCount, prCount = 1, 1
            reactants, products = "", ""
            tempWord = ""
    else:
        print("Invalid equation, make sure the elements are entered correctly.")
        reactantsCount, productsCount = [], []
        reactantsList, productsList = [], []
        reCount, prCount = 1, 1
        reactants, products = "", ""
        tempWord = ""