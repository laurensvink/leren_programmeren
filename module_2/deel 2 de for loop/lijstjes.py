aantal = int(input("Hoeveel lijstjes wil je genereren? "))
lengte = int(input("Hoe lang moet ieder lijstje zijn? "))

alle_lijstjes = []
for i in range(1, aantal + 1):
    lijstje = list(range(i, i + i * lengte, i))
    alle_lijstjes.append(lijstje)
print(alle_lijstjes)
