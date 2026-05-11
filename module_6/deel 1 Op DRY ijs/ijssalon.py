print("Welkom bij Papi Gelato. je mag alle smaken kiezen zolang het maar vanille ijs is.")

def stap2(aantal):
    while True:
        keuze = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")

        if keuze == "hoorntje" or keuze == "bakje":
            return keuze
        else:
            print("Sorry, dat snap ik niet...")

while True:
    while True:
        aantal = input("Hoeveel bolletjes wilt u? ")

        if aantal.isdigit():
            aantal = int(aantal)

            if 1 <= aantal <= 3:
                verpakking = stap2(aantal)

                print(f"Hier is uw {verpakking} met {aantal} bolletje(s).")
                break

            elif 4 <= aantal <= 8:
                print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes")
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
            print("Bedankt en tot ziens!")
            exit()

        else:
            print("Sorry, dat snap ik niet...")