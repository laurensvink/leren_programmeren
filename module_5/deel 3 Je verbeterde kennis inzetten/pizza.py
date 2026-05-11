pizzas = {
    "small": 5,
    "medium": 10,
    "big": 20
}


bestelling = {}


def vraag_aantal(pizza_type):
    try:
        return int(input(f"Hoeveel {pizza_type} pizza's wilt u bestellen? "))
    except:
        print(f"Dat is geen heel getal! Er worden 0 {pizza_type} pizza's gerekend.")
        return 0



for pizza_type in pizzas:
    bestelling[pizza_type] = vraag_aantal(pizza_type)



print("\n************** KASSA BON **************")

totaal = 0

for pizza_type in pizzas:
    aantal = bestelling[pizza_type]
    prijs = pizzas[pizza_type]
    subtotaal = aantal * prijs
    totaal += subtotaal

    if aantal > 0:
        print(f"Pizza's {pizza_type.capitalize():<7}: {aantal} x €{prijs:<2} = €{subtotaal}")

print("----------------------------------------")
print(f"TOTAAL TE BETALEN:              €{totaal}")