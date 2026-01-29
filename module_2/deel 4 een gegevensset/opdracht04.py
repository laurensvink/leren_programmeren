import fruitmand
import random
aantal = int(input("Noem een getal"))

for i in range(aantal):
    gekozen_item = random.choice(fruitmand.fruitmand)
    print(gekozen_item["name"])
