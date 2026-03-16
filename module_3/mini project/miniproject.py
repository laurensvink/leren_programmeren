from random import shuffle

namen = []

# Verzamel namen
while True:
    naam = input("Voer je naam in: ")

    if naam in namen:
        print("Naam bestaat al, probeer opnieuw")
        continue

    namen.append(naam)

    if len(namen) < 3:
        continue

    naam_twee = input("Wil je nog een naam invoeren? (ja/nee) ").lower()
    if naam_twee != "ja":
        break

lootjes = namen.copy()
shuffle(lootjes)

# Zorg dat niemand zijn eigen lootje krijgt
while any(lootjes[i] == namen[i] for i in range(len(namen))):
    shuffle(lootjes)

for _ in range(len(namen)):
    keuze_naam = input("Wie zijn lootje wil je zien? ")
    if keuze_naam in namen:
        i = namen.index(keuze_naam)
        print(f"{keuze_naam} heeft lootje {lootjes[i]}")
    else:
        print("Deze naam staat niet in de lijst. Probeer opnieuw.")