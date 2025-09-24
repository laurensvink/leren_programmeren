from termcolor import colored

mensen = 5
toegang = 7.45
vr_per_5min = 0.37
vr_tijd = 45
vr_kosten = (vr_tijd / 5) * vr_per_5min
kosten_per_persoon = toegang + vr_kosten
totaal = kosten_per_persoon * mensen
jij = totaal / 2
vriend = totaal / 2

print("Jij betaalt:", colored(jij, "blue")) 
print("Je vriend betaalt:", colored(vriend, "blue"))
