def naam_leeftijd():
    name = input("Wat is je naam? ").lower()
    age = int(input("Wat is je leeftijd? "))
    city = input("Wat is je woonplaats? ").lower()
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