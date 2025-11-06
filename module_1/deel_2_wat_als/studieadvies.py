from studieadviestext import *

print(STUDIEDOKTER_TITEL)
input(AANTAL_WEKEN_VRAAG)

stellingen = [
    COMPETENTIE_STELLING_1,
    COMPETENTIE_STELLING_2,
    COMPETENTIE_STELLING_3,
    COMPETENTIE_STELLING_4,
    COMPETENTIE_STELLING_5,
    COMPETENTIE_STELLING_6,
    COMPETENTIE_STELLING_7
]

score = 0
aantal_vragen = 0
altijd_vaak = 0
altijd_vaak_regelmatig = 0

for stelling in stellingen:
    print(stelling)
    antwoord = int(input(OPTIES))
    score += antwoord
    aantal_vragen += 1

    if antwoord <= 1:
        altijd_vaak += 1
    if antwoord <= 2:
        altijd_vaak_regelmatig += 1

gemiddelde = score / aantal_vragen

print(COMPETENTIE_ADVIES_TITEL)

if gemiddelde <= 2 or altijd_vaak > aantal_vragen / 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
elif gemiddelde <= 3 or altijd_vaak_regelmatig > aantal_vragen / 2:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
