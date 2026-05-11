print("Welkom bij Papi Gelato. je mag alle smaken kiezen zolang het maar vanille ijs is.")

prijs_bolletje = 0.95
btw_percentage = 0.06
totaal = 0

def stap2(aantal):
    while True:
        keuze = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")

        if keuze == "hoorntje" or keuze == "bakje":
            return keuze
        else:
            print("Sorry dat is geen optie die we aanbieden...")

while True:
    while True:
        aantal = input("Hoeveel bolletjes wilt u? ")

        if aantal.isdigit():
            aantal = int(aantal)

            if 1 <= aantal <= 3:
                verpakking = stap2(aantal)

                print(f"Hier is uw {verpakking} met {aantal} bolletje(s).")
                subtotaal = aantal * prijs_bolletje
                btw = subtotaal * btw_percentage
                totaal_order = subtotaal + btw
                totaal += totaal_order
                print(f"Dat kost €{totaal_order:.2f} (inclusief {btw_percentage*100}% BTW)")
                break

            elif 4 <= aantal <= 8:
                print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes")
                subtotaal = aantal * prijs_bolletje
                btw = subtotaal * btw_percentage
                totaal_order = subtotaal + btw
                totaal += totaal_order
                print(f"Dat kost €{totaal_order:.2f} (inclusief {btw_percentage*100}% BTW)")
                break

            elif aantal > 8:
                print("Sorry, zulke grote bakken hebben we niet")

        else:
            print("Sorry, dat snap ik niet...")

    while True:
        meer = input("Wilt u nog meer bestellen? ")

        if meer == "ja":
            break

        elif meer == "nee":
            print(f"Bedankt voor uw bestelling. Het totaalbedrag is €{totaal:.2f}")
            exit()

        else:
            print("Sorry, dat snap ik niet...")