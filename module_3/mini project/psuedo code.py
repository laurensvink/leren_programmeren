START

// Initialiseer een lege lijst voor deelnemers
namen = []

WHILE True:
    // Vraag een naam van de deelnemer
    naam = input("Voer naam in: ")

    // Controleer of de naam al bestaat
    IF naam IN namen:
        print("Naam bestaat al, probeer opnieuw.")
        CONTINUE

    // Voeg de naam toe aan de lijst
    namen.append(naam)

    // Als er minder dan 3 namen zijn, blijf vragen
    IF len(namen) < 3:
        CONTINUE

    // Vraag of de gebruiker nog een naam wil invoeren
    nog_een = input("Wil je nog een naam invoeren? (ja/nee): ")
    IF nog_een.lower() != "ja":
        BREAK

// Genereer random lootjes zodat niemand zijn eigen naam krijgt
DO:
    lootjes = shuffle(namen.copy())
WHILE any(lootjes[i] == namen[i] for i in range(len(namen)))

// Print de resultaten
FOR i IN range(len(namen)):
    print(f"{namen[i]} heeft lootje: {lootjes[i]}")

END