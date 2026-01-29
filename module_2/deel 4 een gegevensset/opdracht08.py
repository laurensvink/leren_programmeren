import fruitmand

totaal = 0

for fruit in fruitmand.fruitmand:
    totaal += fruit['weight']

print(totaal)

fruitmand.append({
    'name': 'watermeloen',
    'weight': 5000,
    'color': 'green',
    'round': True
})
