from input import verzamel_gegevens

def main():
    alle_data = verzamel_gegevens()
    
    for persoon in alle_data:
        naam = persoon["name"]
        leeftijd = persoon["age"]
        woonplaats = persoon["city"]
        print(f"Je naam is {naam} en je bent {leeftijd} jaar en je woont in {woonplaats}")


if __name__ == "__main__":
    main()