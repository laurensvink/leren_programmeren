try:
    aantal_small_pizza = int(input("Hoeveel small pizza's wilt u bestellen? "))
except:
    print("Dat is geen heel getal! Er worden 0 small pizza's gerekend.")
    aantal_small_pizza = 0

try:
    aantal_medium_pizza = int(input("Hoeveel medium pizza's wilt u bestellen? "))
except:
    print("Dat is geen heel getal! Er worden 0 medium pizza's gerekend.")
    aantal_medium_pizza = 0

try:
    aantal_big_pizza = int(input("Hoeveel big pizza's wilt u bestellen? "))
except:
    print("Dat is geen heel getal! Er worden 0 big pizza's gerekend.")
    aantal_big_pizza = 0


prijs_small_pizza = 5
prijs_medium_pizza = 10
prijs_big_pizza = 20

gekochte_small_pizza = aantal_small_pizza * prijs_small_pizza
gekochte_medium_pizza = aantal_medium_pizza * prijs_medium_pizza
gekochte_big_pizza = aantal_big_pizza * prijs_big_pizza
totaal = gekochte_small_pizza + gekochte_medium_pizza + gekochte_big_pizza

print("\n************** KASSA BON **************")
if aantal_small_pizza != 0:
    print(f"Pizza's Small:    {aantal_small_pizza} x €5  = €{gekochte_small_pizza}")
if aantal_medium_pizza != 0:
    print(f"Pizza's Medium:   {aantal_medium_pizza} x €10 = €{gekochte_medium_pizza}")
if aantal_big_pizza != 0:
    print(f"Pizza's Big:      {aantal_big_pizza} x €20 = €{gekochte_big_pizza}")
print("----------------------------------------")
print(f"TOTAAL TE BETALEN:              €{totaal}")
