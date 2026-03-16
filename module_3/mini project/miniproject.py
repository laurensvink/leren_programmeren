from random import shuffle

namen = []

while True:
    naam = input("Voer je naam in: ")

    if naam in namen:
        print("Naam bestaat al probeer opnieuw")
        continue

    namen.append(naam)

    if len(namen) < 3:
        continue

    naam_twee = input("Wil je nog een naam invoeren? (ja/nee) ")
    if naam_twee.lower() != "ja":
        break

lootjes = namen.copy()
shuffle(lootjes)

while any(lootjes[i] == namen[i] for i in range(len(namen))):
    shuffle(lootjes)

for i in range(len(namen)):
    print(f"{namen[i]} heeft lootje {lootjes[i]}")