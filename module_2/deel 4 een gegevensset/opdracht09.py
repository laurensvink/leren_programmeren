import fruitmand

fruitmand.fruitmand.pop(4)

printed_colors = []

for fruit in fruitmand.fruitmand:
    color = fruit['color']
    
    if color not in printed_colors:
        print(color)
        printed_colors.append(color)
