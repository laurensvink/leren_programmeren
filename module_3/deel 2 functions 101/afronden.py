month_discount_brands = 'vespanus,tomos,idk'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str) -> str:
    if brand.lower() in month_discount_brands.split(','):
        price_after_discount = price * (1 - MONTH_DISCOUNT_PERC / 100)
        discount = price * MONTH_DISCOUNT_PERC / 100
        
        return f"De nieuwe prijs is: €{price_after_discount:.2f}\nJe discount is: €{discount:.2f}"
    
    return f"€{price:.2f}\nJe hebt geen korting op producten van het merk {brand}."

print(calc_discount(1500, 'Vespanus'))