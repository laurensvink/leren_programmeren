from input import verzamel_gegevens
from termcolor import colored


def main():
    alle_data = verzamel_gegevens()

    for persoon in alle_data:
        naam = persoon["name"].capitalize()
        leeftijd = persoon["age"]
        woonplaats = persoon["city"].capitalize()

        if leeftijd >= 18:
            status = f"die al {leeftijd} jaar volwassen is."
            status_kleur = colored(status, "red")
        else:
            status = "die nog niet volwassen is."
            status_kleur = colored(status, "red")

        woonplaats_kleur = colored(woonplaats, "yellow")
        naam_kleur = colored(naam, "green")

        print(f"In {woonplaats_kleur} woont {naam_kleur}, {status_kleur}")


if __name__ == "__main__":
    main()