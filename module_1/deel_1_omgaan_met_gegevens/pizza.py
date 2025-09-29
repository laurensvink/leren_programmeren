aantal_small_pizza = int(input("hoeveel small pizza's wilt u bestellen?"))
aantal_medium_pizza = int(input("hoeveel medium pizza's wilt u bestellen?"))
aantal_big_pizza = int(input("hoeveel big pizza's wilt u bestellen?"))

prijs_small_pizza = 5
prijs_medium_pizza = 10
prijs_big_pizza = 20 

gekochte_small_pizza = aantal_small_pizza*prijs_small_pizza
gekochte_medium_pizza = aantal_medium_pizza*prijs_medium_pizza
gekochte_big_pizza = aantal_big_pizza*prijs_big_pizza

totaal = gekochte_big_pizza+gekochte_medium_pizza+gekochte_small_pizza

print("************** KASSA BON **************")
print(f"Pizza's Small:              {aantal_small_pizza} x 5 = €{gekochte_small_pizza}")
print(f"Pizza's Medium:            {aantal_medium_pizza} x 10 = €{gekochte_medium_pizza}")
print(f"Pizza's Big:               {aantal_big_pizza} x 20 = €{gekochte_big_pizza}")
print("--------------------------------------")
print(f"Te betalen                         €{totaal}")
