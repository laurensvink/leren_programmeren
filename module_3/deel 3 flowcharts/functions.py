#defineer hieronder je functies
import random

score = 0
ronde = 1
MAX_RONDEN = 20

while ronde <= MAX_RONDEN:

    print(f"\n--- Ronde {ronde} ---")

    geheim = random.randint(1, 1000)
    beurten = 1
    geraden = False

    while beurten <= 10:
        gok = int(input("Raad het getal (1-1000): "))

        if gok == geheim:
            print("Geraden!")
            score += 1
            geraden = True
            break

        elif gok < geheim:
            print("Hoger")
        else:
            print("Lager")

        verschil = abs(gok - geheim)

        if verschil < 20:
            print("Je bent heel warm")
        elif verschil < 50:
            print("Je bent warm")

        beurten += 1

    if not geraden:
        print(f"Je hebt het getal niet geraden. Het was {geheim}")

    print(f"Score tot nu toe: {score}")

    if ronde == MAX_RONDEN:
        break

    doorgaan = input("Nog een getal raden? (ja/nee): ").lower()
    if doorgaan != "ja":
        break

    ronde += 1

print(f"\nEindscore: {score}")


#defineer hierboven je functies

if __name__ == "__main__":
    import application

