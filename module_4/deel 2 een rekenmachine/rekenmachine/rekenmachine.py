from functions import *

print("Wat wilt u doen?")
choice = input("A) optellen, B) aftrekken, C) vermenigvuldigen, D) delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren: ").lower()

# Eerste berekening
if choice in ["a", "b", "c", "d"]:
    n1 = float(input("Geef me het eerste getal: "))
    n2 = float(input("Geef me het tweede getal: "))
elif choice in ["e", "f", "g", "h"]:
    n1 = float(input("Geef me het getal: "))
    if choice in ["e", "f"]:
        n2 = 1
    else:
        n2 = 2

# Berekening uitvoeren
if choice == "a":
    result = addition(n1, n2)
elif choice == "b":
    result = subtraction(n1, n2)
elif choice == "c":
    result = multiplication(n1, n2)
elif choice == "d":
    result = division(n1, n2)
elif choice == "e":
    result = addition(n1, n2)
elif choice == "f":
    result = subtraction(n1, n2)
elif choice == "g":
    result = multiplication(n1, n2)
elif choice == "h":
    result = division(n1, n2)

print("De uitkomst is:", result)

while True:
    choice = input(f"\nWil je wat met de uitkomst ({result}) doen?\n"
                   "A) optellen, B) aftrekken, C) vermenigvuldigen, D) delen,\n"
                   "E) ophogen, F) verlagen, G) verdubbelen, H) halveren, I) stoppen: ").lower()

    if choice == "i":
        print("Programma gestopt.")
        break

    n1 = result

    if choice in ["a", "b", "c", "d"]:
        n2 = float(input("Geef me het tweede getal: "))
    elif choice in ["e", "f"]:
        n2 = 1
    elif choice in ["g", "h"]:
        n2 = 2
    else:
        print("Ongeldige keuze!")
        continue

    if choice == "a":
        result = addition(n1, n2)
    elif choice == "b":
        result = subtraction(n1, n2)
    elif choice == "c":
        result = multiplication(n1, n2)
    elif choice == "d":
        result = division(n1, n2)
    elif choice == "e":
        result = addition(n1, n2)
    elif choice == "f":
        result = subtraction(n1, n2)
    elif choice == "g":
        result = multiplication(n1, n2)
    elif choice == "h":
        result = division(n1, n2)

    print("Nieuwe uitkomst:", result)