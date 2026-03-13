PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na

leeftijd = int(input("Hoe oud ben je? "))

if leeftijd < 18:
    print("je bent nog niet oud genoeg.")
    wachten = 18-leeftijd
    print(f"probeer het over {wachten} jaar opnieuw")
    exit()
elif leeftijd > 18:
    naam = input("wat is je naam? ")
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = "blauw"
        elif leeftijd < 21:
            bandje = "rood"
        print(f"je krijgt van mij een {bandje} bandje")
    elif leeftijd >= 21:
        print("je krijgt van mij een mooie stempel.")
        stempel = True
        bandje = False
drankje = input("wat wil je drinken? ")
if drankje == "cola":
    if bandje == "rood" or bandje == "blauw":
        print("Alsjeblieft complimenten van het huis.")
        exit()
    else:
        print(f"alsjeblieft je {drankje} dat is dan {PRIJS_COLA}")
if drankje == "bier":
    if stempel == True or bandje == "blauw" or  bandje == "rood":
        if bandje == "rood" or bandje == "blauw":
            print("Alsjeblieft complimenten van het huis.")
        else:
            print(f"alsjeblieft je {drankje} dat is dan {PRIJS_BIER}")
    else:
        print("sorry je mag geen alcohol bestellen onder de 21.")
        wachten = 21-leeftijd
        print(f"probeer het over {wachten} jaar opnieuw")
        exit()
if drankje == "champagne":
    if bandje == "blauw" or bandje == "rood":
        if bandje == "blauw":
            print(f"alsjeblieft je {drankje} dat is dan {PRIJS_CHAMPAGNE}")
        else:
            print("sorry je mag geen alcohol bestellen onder de 21.")
            wachten = 21-leeftijd
            print(f"probeer het over {wachten} jaar opnieuw")
            exit()
    else:
        print("sorry alleen vips mogen Champagne bestellen. ")
        exit()
if drankje not in DRANKJES:
    print("sorry geen idee wat je bedoelt hier heb je een glaasje water. ")