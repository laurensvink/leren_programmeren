from studieadviestext import *
score = 0 

print(STUDIEDOKTER_TITEL)
input(AANTAL_WEKEN_VRAAG)
print(COMPETENTIE_STELLING_1)
score += int(input(OPTIES))
print(COMPETENTIE_STELLING_2)
score += int(input(OPTIES))
print(COMPETENTIE_STELLING_3)
score += int(input(OPTIES))
print(COMPETENTIE_STELLING_4)
score += int(input(OPTIES))
print(COMPETENTIE_STELLING_5)
score += int(input(OPTIES))
print(COMPETENTIE_STELLING_6)
score += int(input(OPTIES))
print(COMPETENTIE_STELLING_7)
score += int(input(OPTIES))
gemiddelde = score/7

print(COMPETENTIE_ADVIES_TITEL)
if gemiddelde <= 2 :
    print(COMPETENTIE_ADVIES_ZORGELIJK)
if gemiddelde <= 3 :
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else :
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)