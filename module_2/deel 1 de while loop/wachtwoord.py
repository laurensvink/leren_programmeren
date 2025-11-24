ww = "linkerkoplamp69"

ap = 0
while ap <5:
    ap += 1 
    iww = input("Voer het wachtwoord in!")
    if iww == ww:
        print(f"Je hebt het wachtwoord geraden in {ap}pogingen")
else:
    print("je hebt het wachtwoord na 5 pogingen niet geraden je bent verbannen!")