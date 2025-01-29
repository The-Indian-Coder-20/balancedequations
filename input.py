import re
import validElementChecker


reCount, prCount = 1, 1
reactantsCount, productsCount = [], []
valid_equation = re.compile(r'^[A-Za-z0-9()]+$')
mainKey = True
tempCount = 0
lastBracketIndex = 0

reactantsList, productsList = [], []
finalReactantsCount, finalProductsCount = [], []

print("""If there is only one atom of the element, please input the number '1' after the element. (E.g. Na1).
""")


#Input parsing has been completed for regular chemical equations as well as those with parentheses.
tempWord = ""
tempNum = ""
reactantKey = True

while mainKey:

    while reactantKey:
        tempNum, tempWord = "", ""
        reactant = input(f"What is reactant #{reCount}?: ")
        if reactant == "":
            break
        reactantsList.append(reactant)
        tempReactant = reactant
        reCount += 1
        while len(tempReactant) > 0:
            if tempReactant[0].isalpha():
                if len(tempNum) != 0:
                    reactantsCount.append(int(tempNum))
                    tempNum = ""
                tempWord += tempReactant[0]
                tempReactant = tempReactant[1:]
            elif tempReactant[0].isdigit():
                if len(tempWord) != 0:
                    reactantsCount.append(tempWord)
                tempNum += tempReactant[0]
                if len(tempReactant) == 1:
                    reactantsCount.append(int(tempNum))
                tempReactant = tempReactant[1:]
                tempWord = ""
            elif tempReactant[0] == "(":
                if len(tempNum) != 0:
                    reactantsCount.append(int(tempNum))
                tempReactant = tempReactant[1:]
                tempNum, tempWord = "", ""
                while tempReactant[0] != ")":
                    if tempReactant[0].isalpha():
                        if len(tempNum) != 0:
                            reactantsCount.append(int(tempNum) * int(tempReactant[(tempReactant.index(")") + 1)]))
                            tempNum = ""
                        tempWord += tempReactant[0]
                        tempReactant = tempReactant[1:]
                    elif tempReactant[0].isdigit():
                        reactantsCount.append(tempWord)
                        tempNum += tempReactant[0]
                        tempReactant = tempReactant[1:]
                        if tempReactant[0] == ")":
                            reactantsCount.append(int(tempNum) * int(tempReactant[(tempReactant.index(")") + 1)]))
                        tempWord = ""
                    elif tempReactant[0] == ")":
                            break
                tempReactant = tempReactant[(tempReactant.index(")") + 2):]
                tempNum = ""
        finalReactantsCount.append(reactantsCount)
        reactantsCount = []

    tempWord = ""
    tempNum = ""
    productKey = True

    while productKey:
        tempNum, tempWord = "", ""
        product = input(f"What is product #{prCount}?: ")
        if product == "":
            break
        productsList.append(product)
        tempProduct = product
        prCount += 1
        while len(tempProduct) > 0:
            if tempProduct[0].isalpha():
                if len(tempNum) != 0:
                    productsCount.append(int(tempNum))
                    tempNum = ""
                tempWord += tempProduct[0]
                tempProduct = tempProduct[1:]
            elif tempProduct[0].isdigit():
                if len(tempWord) != 0:
                    productsCount.append(tempWord)
                tempNum += tempProduct[0]
                if len(tempProduct) == 1:
                    productsCount.append(int(tempNum))
                tempProduct = tempProduct[1:]
                tempWord = ""
            elif tempProduct[0] == "(":
                if len(tempNum) != 0:
                    productsCount.append(int(tempNum))
                tempProduct = tempProduct[1:]
                tempNum, tempWord = "", ""
                while tempProduct[0] != ")":
                    if tempProduct[0].isalpha():
                        if len(tempNum) != 0:
                            productsCount.append(int(tempNum) * int(tempProduct[(tempProduct.index(")") + 1)]))
                            tempNum = ""
                        tempWord += tempProduct[0]
                        tempProduct = tempProduct[1:]
                    elif tempProduct[0].isdigit():
                        productsCount.append(tempWord)
                        tempNum += tempProduct[0]
                        tempProduct = tempProduct[1:]
                        if tempProduct[0] == ")":
                            productsCount.append(int(tempNum) * int(tempProduct[(tempProduct.index(")") + 1)]))
                            tempNum = ""
                        tempWord = ""
                    elif tempProduct[0] == ")":
                            break
                tempProduct = tempProduct[(tempProduct.index(")") + 2):]
                tempNum = ""
        finalProductsCount.append(productsCount)
        productsCount = []

    reactants, products = "", ""

    if all(valid_equation.fullmatch(item) for item in reactantsList) and all(valid_equation.fullmatch(item) for item in productsList):
        for i in reactantsList:
            if reactantsList.index(i) != len(reactantsList) - 1:
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
            finalProductsCount, finalReactantsCount = [], []
            reactantsList, productsList = [], []
            reCount, prCount = 1, 1
            reactants, products = "", ""
            tempWord = ""
    else:
        print("Invalid equation, make sure the elements are entered correctly.")
        reactantsCount, productsCount = [], []
        finalProductsCount, finalReactantsCount = [], []
        reactantsList, productsList = [], []
        reCount, prCount = 1, 1
        reactants, products = "", ""
        tempWord = ""