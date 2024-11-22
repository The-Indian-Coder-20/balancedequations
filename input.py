import re

key = True

valid_equation = re.compile(r'^[A-Za-z0-9+ ]+$')

while key:
    reactants = (input("""What are the reactants? (... + ...):
""")).strip()
    products = (input("""What are the products? (... + ...)?:
""")).strip()

    if valid_equation.match(reactants) and valid_equation.match(products):
        print(f"The entered chemical equation is {reactants} -> {products}")
        correctornot = input("Is this the correct input? [y/n]  ")
        if correctornot.lower() == "y":
            key = False
        else:
            print("Please re-enter the chemical equation")
    else:
        print("Chemical equation has invalid characters. Please use only letters, numbers, +, and spaces.")
        
for i in reactants:
    if not i.isalnum():
        reactants = reactants.replace(i, "")
for i in products:
    if not i.isalnum():
        products = products.replace(i, "")
