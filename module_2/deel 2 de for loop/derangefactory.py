aantal_lijsten = int(input("Hoeveel lijstjes wilt u zien? "))

resultaat = []

for i in range(1, aantal_lijsten + 1):
    lengte = int(input(f"Hoelang moet lijst {i} zijn? "))

    if i == 1:
        lijst = list(range(1, lengte + 1))
    elif i == 2:
        lijst = [2 * x for x in range(1, lengte + 1)]
    elif i == 3:
        lijst = [3 * x for x in range(1, lengte + 1)]
    else:
        lijst = list(range(1, lengte + 1))

    resultaat.append(lijst)

print(resultaat)
