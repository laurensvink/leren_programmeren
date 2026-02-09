import fruitmand

totaal = 0

for fruit in fruitmand.fruitmand:
    totaal += fruit['weight']

print(totaal)

fruitmand.fruitmand.append({
    'name': 'watermeloen',
    'weight': 5000,
    'color': 'green',
    'round': True
})

nieuw_totaal = 0 

for fruit in fruitmand.fruitmand:
    nieuw_totaal += fruit['weight']

print(nieuw_totaal)