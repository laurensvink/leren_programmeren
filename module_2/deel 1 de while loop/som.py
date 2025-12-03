totaal = 0
optel_getal = 50
eind = 1000
rekensom = ""
stap = 1

while totaal <= eind:
    totaal += optel_getal
    rekensom += f"{optel_getal} + "
    nette_rekensom = rekensom[:-3]

    print(f"{stap}. {nette_rekensom} = {totaal}")

    optel_getal += 1
    stap += 1
