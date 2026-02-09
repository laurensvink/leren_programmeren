from fruitmand import fruitmand

def gewicht_van_fruit(fruit):
    return fruit['weight']

gesorteerd_fruit = sorted(fruitmand, key=gewicht_van_fruit, reverse=True)

for fruit in gesorteerd_fruit:
    gewicht_kg = fruit['weight'] / 1000
    print(fruit['name'], ":", gewicht_kg, "kg")
