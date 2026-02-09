import time, math, random
player_attack = 1
player_defense = 0
player_health = 3
item = "niks"
sleutel = False
mag_nog_kamer8 = True


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('en de deur gaat piepend voor je neus open.')
time.sleep(1)


# === [kamer 7] === #
print("Welkom")
if random.randint(1, 10) == 1:
    print("Helaas, vandaag geen rupee voor jou")
    rupee = 0
else:
    print("Hier heb je een gratis rupee!")
    print("Bewaar hem goed, je hebt de rupee later nodig.")
    rupee = 1
print("er zijn 2 deuren in deze kamer! ")
deur_keuze_kamer7 = input("Toets 1 om rechtdoor te gaan! toets 2 om rechtaf te gaan!")
if deur_keuze_kamer7 == "1":
    # === [kamer 2] === #
    getal1 = random.randint(10, 25)
    getal2 = random.randint(-5, 75)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        juist_antwoord = getal1 + getal2
    elif operator == '-':
        juist_antwoord = getal1 - getal2
    else:  # operator == '*'
        juist_antwoord = getal1 * getal2
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toetsen 9 t/m 0.')
    print(f'Daarboven zie je een som staan: {getal1}{operator}{getal2}=?')
    antwoord = int(input('Wat toets je in? '))
    if antwoord == juist_antwoord:
        print('Het standbeeld laat de rupee vallen en je pakt hem op!')
        rupee += 1
    else:
        print('Er gebeurt niets....')
    print('Je ziet een deur achter het standbeeld.')
    print("je ziet nog een deur aan de zijkant van de kamer. je kan kiezen welke deur je wilt.")
    deur_keuze = input("welke deur kies je? wil je naar kamer 8 of 6? toets voor kamer 6-> 1 en voor kamer 8-> 2 ")
    if deur_keuze == "1":


        # === [kamer 6] === #
        zombie_attack = 2
        zombie_defense = 0
        zombie_health = 3

        zombie_hit_damage = max(1, zombie_attack - player_defense)
        player_hit_damage = max(1, player_attack - zombie_defense)

        zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
        player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        player_health -= zombie_attack

        if player_attack_amount < zombie_attack_amount:
            print(f'In {player_attack_amount} rondes versla je de zombie.')
            print(f'Je health is nu {player_health}.')
        kamer_keuze_6 = input("kamer 3 of kamer 8")
        if kamer_keuze_6 == "3":
            mag_nog_kamer8 = False


    # === [kamer 8] === 
    if mag_nog_kamer8 == True:
        print("welkom in de gok kamer!")
        print("hier kan je rupee's gokkken! je gokt 1 rupee er worden 2 dobbelstenen gegooit.")
        print("DE JACKPOT! is het aantal ogen van de dobbelstenen pricies 7? Dan win je 1 rupee EN krijg je 4 health erbij")
        print("alles boven 7 ogen totaal Dan verdubbel je je rupee's!")
        print("maar... verlies je... dan verlies je 1 health!")
        gok_keuze = input("wil je gokken?")
        if gok_keuze == "ja":
            worp_1 = random.randint(1, 6)
            print(f"Je hebt gegooid: {worp_1}")
            worp_2 = random.randint(1,6)
            print(f"Je hebt gegooid: {worp_2}")
            totaal = worp_1 + worp_2
            print(totaal)
            if totaal == 7:
                print("DE JACKPOT!!!")
                print("je hebt 1 rupee en 4 health gewonnen!")
                rupee += 1
                player_health += 4  
                time.sleep(1)
            elif totaal < 7:
                print("je hebt verloren je verliest 1 health")
                player_health -= 1 
                time.sleep(1)
            else :
                print("je hebt je rupee's verdubbeld!")
                rupee *= 2  
                time.sleep(1)
                keuze_kamer8 = input("Er zijn weer 2 deuren: linksaf of rechtsaf? ")
                if keuze_kamer8 == "rechtsaf":
                    # === [kamer 9] === #
                    print("Welkom in deze betoverde kamer...")
                    keuze = random.choice(["defence", "health"])
                    if keuze == "defence":
                        player_defense += 1
                        print("De magie versterkt je verdediging! +1 defence.")
                    else:
                        player_health += 2
                        print("De magie geneest je lichaam! +2 health.")


# === [kamer 3] === #
print("Welkom in de Shop!")
print("Je kunt hier een zwaard, schild of sleutel kopen!")
print("Een zwaard of schild kost 1 rupee, sleutel kost 2.")
print(f"Je hebt {rupee} rupee(s).")

if rupee >= 2:
    print("Je koopt een zwaard en schild voor 2 rupees.")
    rupee -= 2
    item = ["schild", "zwaard"]
else:
    kopen = input("Toets 1 voor zwaard, 2 voor schild, 3 voor sleutel, 4 voor niks: ")
    if kopen == "1":
        item = "zwaard"
        rupee -= 1
    elif kopen == "2":
        item = "schild"
        rupee -= 1
    elif kopen == "3":
        sleutel = True
        rupee -= 2
    else:
        item = "niks"


# === [kamer 4] === #
Boycke_attack = 2
Boycke_defense = 0
Boycke_health = 3
if item == "niks":
    print("Dapper loop je de kamer binnen.")
    print('Je loopt tegen een Boycke aan.')
else :    
    print(f'Dapper met je nieuwe {item} loop je de kamer binnen.')
    print('Je loopt tegen een Boycke aan.')
Boycke_hit_damage = (Boycke_attack - player_defense)
if Boycke_hit_damage <= 0:
    print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
else:
    Boycke_attack_amount = math.ceil(player_health / Boycke_hit_damage)  
    player_hit_damage = (player_attack - Boycke_defense)
    player_attack_amount = math.ceil(Boycke_health / player_hit_damage)
    player_health -= (Boycke_attack_amount - (Boycke_attack_amount - player_attack_amount)) * Boycke_hit_damage
    if player_attack_amount < Boycke_attack_amount:
        print(f'In {player_attack_amount} rondes versla je de zombie.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de Boycke te sterk voor je.')
        print('Game over.')
        exit()
print('')


# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel is True :
    print("je opent de kist en ziet een gloednieuwe camera! ")
else :
    print("je hebt geen sleutel om de kist mee te openen! ")