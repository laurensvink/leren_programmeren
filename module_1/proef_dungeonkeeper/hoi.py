import time, math, random

# === [SPELER STATISTIEKEN] === #
player = {
    "attack": 1,
    "defense": 0,
    "health": 3,
    "rupee": 0,
    "item": [],
    "sleutel": False
}


# === [HULPFUNCTIES] === #
def pause(sec=1):
    time.sleep(sec)


def print_stats():
    print(f"\n❤️ Health: {player['health']} | 🪙 Rupees: {player['rupee']} | 🛡️ Defense: {player['defense']} | ⚔️ Attack: {player['attack']}\n")


def shop():
    """Kamer 3 - Winkel"""
    print("\n🛒 Welkom in de Shop!")
    print("Een zwaard of schild kost 1 rupee, een sleutel kost 2 rupees.")
    print_stats()

    if player["rupee"] >= 2:
        keuze = input("Wil je een zwaard en schild kopen voor 2 rupees? (ja/nee): ").lower()
        if keuze == "ja":
            player["rupee"] -= 2
            player["item"] = ["zwaard", "schild"]
            print("Je hebt een zwaard en schild gekocht!")
            return
    kopen = input("1 = zwaard, 2 = schild, 3 = sleutel, 4 = niks: ")

    if kopen == "1" and player["rupee"] >= 1:
        player["item"].append("zwaard")
        player["rupee"] -= 1
        player["attack"] += 1
        print("Je koopt een zwaard!")
    elif kopen == "2" and player["rupee"] >= 1:
        player["item"].append("schild")
        player["rupee"] -= 1
        player["defense"] += 1
        print("Je koopt een schild!")
    elif kopen == "3" and player["rupee"] >= 2:
        player["sleutel"] = True
        player["rupee"] -= 2
        print("Je koopt een sleutel!")
    else:
        print("Je koopt niets.")


def gok_kamer():
    """Kamer 8 - Gokken met dobbelstenen"""
    print("\n🎲 Welkom in de gok kamer!")
    print("Je gokt 1 rupee. Er worden 2 dobbelstenen gegooid.")
    print("7 ogen = JACKPOT! (+1 rupee, +4 health)")
    print("Meer dan 7 = rupees verdubbelen")
    print("Minder dan 7 = -1 health")

    if player["rupee"] < 1:
        print("Je hebt geen rupees om te gokken!")
        return

    if input("Wil je gokken? (ja/nee): ").lower() != "ja":
        return

    worp_1 = random.randint(1, 6)
    worp_2 = random.randint(1, 6)
    totaal = worp_1 + worp_2
    print(f"Je gooide {worp_1} en {worp_2} (totaal: {totaal})")

    if totaal == 7:
        print("🎉 JACKPOT! +1 rupee en +4 health!")
        player["rupee"] += 1
        player["health"] += 4
    elif totaal > 7:
        print("Dubbel geluk! Je verdubbelt je rupees!")
        player["rupee"] *= 2
    else:
        print("Verloren! -1 health.")
        player["health"] -= 1
    pause()


def betoverde_kamer():
    """Kamer 9 - Magische kamer"""
    print("\n✨ Welkom in de betoverde kamer...")
    keuze = random.choice(["defense", "health"])
    if keuze == "defense":
        player["defense"] += 1
        print("De magie versterkt je verdediging! (+1 defence)")
    else:
        player["health"] += 2
        print("De magie geneest je! (+2 health)")
    pause()


def vecht_vijand(naam, attack, defense, health):
    """Simpele gevechtsfunctie"""
    print(f"\n⚔️ Je vecht tegen een {naam}!")
    vijand_hit = max(1, attack - player["defense"])
    speler_hit = max(1, player["attack"] - defense)

    rondes_speler = math.ceil(health / speler_hit)
    rondes_vijand = math.ceil(player["health"] / vijand_hit)

    if rondes_speler <= rondes_vijand:
        print(f"Je verslaat de {naam} in {rondes_speler} rondes!")
        player["health"] -= vijand_hit * (rondes_speler - 1)
        print(f"Je overleeft met {player['health']} health.")
        return True
    else:
        print(f"De {naam} is te sterk... 💀")
        print("Game Over.")
        exit()


# === [SPEL START] === #
print("🏰 Door de grote deuren stap je de gang binnen. Het ruikt muf en vochtig...")
pause(1)
print("Een deur opent langzaam voor je neus...")
pause(1)

# === [KAMER 7] === #
print("\n🎉 Welkom in kamer 7!")
if random.randint(1, 10) == 1:
    print("Helaas, geen rupee voor jou.")
else:
    print("Je krijgt een gratis rupee!")
    player["rupee"] += 1
pause()

print("Er zijn 2 deuren in deze kamer.")
deur = input("1 = rechtdoor, 2 = rechtsaf: ")

# === [ROUTE 1: KAMER 2 -> GOKKEN -> SHOP] === #
if deur == "1":
    print("\nJe stapt door de deur en ziet een standbeeld met een som...")
    a, b = random.randint(10, 25), random.randint(-5, 75)
    op = random.choice(['+', '-', '*'])
    juist = eval(f"{a}{op}{b}")
    print(f"Som: {a}{op}{b}=?")
    try:
        antwoord = int(input("Wat toets je in? "))
        if antwoord == juist:
            print("✅ Correct! Je krijgt een rupee!")
            player["rupee"] += 1
        else:
            print("❌ Fout. Niets gebeurt...")
    except ValueError:
        print("Ongeldige invoer!")

    deur2 = input("Je ziet twee deuren: 8 of 6? ")

    if deur2 == "8":
        gok_kamer()
    else:
        vecht_vijand("Zombie", 2, 0, 3)

    # Na het gevecht of gokken:
    keuze = input("Linksaf of rechtsaf? ")
    if keuze == "links":
        shop()
    else:
        betoverde_kamer()

# === [ROUTE 2: KAMER 8 DIRECT] === #
else:
    gok_kamer()
    keuze = input("Linksaf of rechtsaf? ")
    if keuze == "links":
        shop()
    else:
        betoverde_kamer()

# === [KAMER 4 - BOSS] === #
vecht_vijand("Boycke", 2, 0, 3)

# === [KAMER 5 - SCHATKIST] === #
print("\n💎 Je vindt een grote schatkist in het midden van de kamer!")
if player["sleutel"]:
    print("Je opent de kist met je sleutel... Binnenin ligt een gloednieuwe camera! 📸")
else:
    print("De kist is op slot... Je hebt geen sleutel.")
pause(1)

print("\n🏆 Einde van het avontuur!")
print_stats()
print("Bedankt voor het spelen!")
