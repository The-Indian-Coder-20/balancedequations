import re

reCount, prCount = 1, 1
reactantsCount, productsCount = [], []
tempWord = ""
valid_equation = re.compile(r'^[A-Za-z0-9+ ()]+$')
mainKey = True

while mainKey:

    key = True

    while key:
        reactant = input(f"What is reactant {reCount}? (...#): ")
        if reactant != "":
            reCount += 1
            for i in reactant:
                if i.isalpha():
                    tempWord += i
            reactantsCount.append(tempWord)
            tempWord = ""
            if i in "123456789":
                reactantsCount.append(reactant[reactant.index(i):])
        else:
            key = False
            if len(reactantsCount) == 0:
                print("No reactants entered. Please re-enter the chemical equation")
                key = True

    key = True

    while key:
        product = input(f"What is product {prCount}? (...#): ")
        if product != "":
            prCount += 1
            for i in product:
                if i.isalpha():
                    tempWord += i
            productsCount.append(tempWord)
            tempWord = ""
            if i in "123456789":
                productsCount.append(product[product.index(i):])             
        else:
            key = False
            if len(productsCount) == 0:
                print("No products entered. Please re-enter the chemical equation")
                key = True

    reactants, products = "", ""

    if all(valid_equation.fullmatch(item) for item in reactantsCount) and all(valid_equation.fullmatch(item) for item in productsCount):
        if len(reactantsCount) == 1:
            reactants = reactantsCount[0]
        else:
            for i in range(len(reactantsCount)):
                if reactantsCount[i].isalpha():
                    if i == len(reactantsCount) - 1:
                        word = reactantsCount[i]
                        reactants += word
                    elif reactantsCount[i+1].isalpha():
                        word = reactantsCount[i]
                        reactants += word
                        if i != len(reactantsCount) - 1:
                            reactants += " + "
                    elif reactantsCount[i+1] in "123456789":
                        word = reactantsCount[i] + reactantsCount[i+1]
                        reactants += word
                        if i != len(reactantsCount) - 2:
                            reactants += " + "
        if len(productsCount) == 1:
            products = productsCount[0]
        else:
            for i in range(len(productsCount)):
                if productsCount[i].isalpha():
                    if i == len(productsCount) - 1:
                        word = productsCount[i]
                        products += word
                    elif productsCount[i+1].isalpha():
                        word = productsCount[i]
                        products += word
                        if i != len(productsCount) - 2:
                            products += " + "
                    elif productsCount[i+1] in "123456789":
                        word = productsCount[i] + productsCount[i+1]
                        products += word
                        if i != len(productsCount) - 2:
                            products += " + "
        print(f"The entered equation is {reactants} => {products}")
        mainKey = False
    else:
        print("Invalid equation, make sure the elements are entered correctly.")
        reactantsCount, productsCount = [], []
        reCount, prCount = 1, 1