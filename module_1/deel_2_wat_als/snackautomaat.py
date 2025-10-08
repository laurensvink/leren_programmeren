print("Welkom bij het snackautomaat!")
print("Toets alle gewilde snacks achter elkaar in!")
print("a voor een chocolade reep")
print("b voor een zakje chips")
print("c voor een blikje cola")
print("d voor een pakje kauwgom")
print("e voor een flesje water")
snacks = input("Wat wil je graag hebben? ")

gevonden = False  # om te checken of er iets is gekozen

if "a" in snacks:
    print("Alsjeblieft, hier is je chocolade reep!")
    gevonden = True
if "b" in snacks:
    print("Alsjeblieft, hier is je zakje chips!")
    gevonden = True
if "c" in snacks:
    print("Alsjeblieft, hier is je blikje cola!")
    gevonden = True
if "d" in snacks:
    print("Alsjeblieft, hier is je pakje kauwgom!")
    gevonden = True
if "e" in snacks:
    print("Alsjeblieft, hier is je flesje water!")
    gevonden = True

if not gevonden:
    print("Maak een geldige keuze!!!")
