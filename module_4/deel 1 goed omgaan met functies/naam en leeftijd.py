def naam_leeftijd():
    name = input("Wat is je naam? ").lower()
    age = int(input("Wat is je leeftijd? "))
    city = input("wat is je woonplaats? ").lower()
    return {"name": name, "age": age, "city": city}


def verzamel_gegevens():
    resultaten = []

    while True:
        data = naam_leeftijd()
        resultaten.append(data)

        doorgaan = input("Toets enter om door te gaan of stop om te printen: ").lower()
        if doorgaan == "stop":
            break

    return resultaten

alle_data = verzamel_gegevens()

for persoon in alle_data:
    naam = persoon["name"]
    leeftijd = persoon["age"]
    woonplaats = persoon["city"]
    print(f"je naam is {naam} en je bent {leeftijd} jaar en je woont in {woonplaats}")