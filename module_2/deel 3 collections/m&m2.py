import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]

aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))

zak = {

}

for _ in range(aantal):
    kleur = random.choice(kleuren)

    if kleur in zak:
        zak[kleur] += 1
    else:
        zak[kleur] = 1


print("De zak met M&M's:")
print(zak)
