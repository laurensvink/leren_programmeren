boodschappen = {}

meer = "ja"

while meer == "ja":
    artikel = input("Welk artikel wil je toevoegen? ")
    aantal = int(input("Hoeveel wil je toevoegen? "))

    if artikel in boodschappen:
        boodschappen[artikel] = boodschappen[artikel] + aantal
    else:
        boodschappen[artikel] = aantal

    meer = input("Wil je nog meer boodschappen toevoegen? (ja/nee) ")

print("Boodschappenlijst:")

for artikel in boodschappen:
    print(artikel, ":", boodschappen[artikel])

print("Einde")