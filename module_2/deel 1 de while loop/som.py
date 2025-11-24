totaal = 50
optel_getal = totaal
#start = 50
eind = 1000
rekensom = ""
while totaal < eind:
    optel_getal+=1
    rekensom += f"{totaal}+"
    totaal = totaal+optel_getal
    print(totaal)
    print(rekensom)  