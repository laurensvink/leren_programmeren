print("ik ga je cocktail raden door middel van een aantal vragen ")
print("beantwoord de vragen met ja of nee ")

antwoord_1 = input("Zit er rood in het drankje? ")

if antwoord_1 == "ja":
    antwoord_2 = input("Zit het drankje in een laag glas? ")
    if antwoord_2 == "ja":
        print("Je drankje is een Negroni")
    else:
        antwoord_3 = input("is het in een middelhoog glas?")
        if antwoord_3 == "ja" :
            print("je drankje is een spritz.")
        else :
            print("je drankje is een french martini.")
        
elif antwoord_1 == "nee":
    antwoord_4 = input("Is je drankje groen? ")
    if antwoord_4 == "ja":
        print("Je drankje is een mojito")
    else:
        antwoord_5 = input("Heeft je drankje meerdere kleuren? ")
        if antwoord_5 == "ja":
            print("Je drankje is een Kiv")
        else:
            antwoord_6 = input("Is je drankje geelachtig? ")
            if antwoord_6 == "ja":
                antwoord_7 = input("Zit je drankje in een cocktailglas? ")
                if antwoord_7 == "ja":
                    print("Je drankje is een White Lady")
                else:
                    print("Je drankje is een Fizz")
            else:
                print("Je drankje is een French Connection")
       

    
  
