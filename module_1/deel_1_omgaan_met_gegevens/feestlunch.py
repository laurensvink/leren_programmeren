prijs_croissant = 0.39
prijs_stokbrood = 2.78
kortingsbon = 0.50
aantal_croissant = 17
aantal_stokbrood = 2
aantal_kortingsbon = 3

totaal_croissant = aantal_croissant * prijs_croissant
totaal_stokbrood = aantal_stokbrood * prijs_stokbrood
totaal_korting = aantal_kortingsbon * kortingsbon

totaal_prijs = totaal_croissant + totaal_stokbrood - totaal_korting

print(f"lunch kost in totaal: €{totaal_prijs:.2f}")
