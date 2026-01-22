vertaling = {
    "noob": "pro",
    "verloren": "gewonnen",
    "uren": "minuten",
    "Family friendly": "Toxic",
    "banned": "verbannen"
}

verhaal = """verhaal = "Op een regenachtige middag speelde een noob een online spel in zijn kamer.
Hij dacht dat hij alles begreep, maar na uren oefenen had hij nog steeds verloren.
Zijn vrienden lachten zachtjes, maar bleven family friendly om niemand te kwetsen.
Plots maakte hij een slimme zet die niemand had verwacht.
De overwinning was dichtbij en zijn zelfvertrouwen groeide.
Toch gebruikte hij per ongeluk een truc die eigenlijk banned was.
Het spel stopte abrupt en het scherm werd zwart.
Teleurgesteld zuchtte hij, maar hij leerde een belangrijke les.
Met geduld en eerlijk spelen zou hij de volgende keer beter zijn.
En zo eindigde de dag met hoop, ondanks alles wat verloren leek.
"""
woorden = verhaal.lower().split()

vertaalde_woorden = []
for woord in woorden:
    if woord in vertaling:
        vertaalde_woorden.append(vertaling[woord])
    else:
        vertaalde_woorden.append(woord)

resultaat = " ".join(vertaalde_woorden)
print("Hertaling:")
print(resultaat)