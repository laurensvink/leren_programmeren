import random
kleuren = ("oranje", "blauw", "groen", "bruin")


aantal = int(input("Hoeveel M&M's moeten er in de zak? "))


def vul_zak(aantal_mmms):
    zak = [] 
    for _ in range(aantal_mmms):
        zak.append(random.choice(kleuren))
    return zak
zak_met_mmms = vul_zak(aantal)
print("Inhoud van de zak met M&M's:")
print(zak_met_mmms)