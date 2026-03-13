print("welkom bij de kaasrader")
print("Hier ga ik de kaas die je in gedachte hebt raden ")

geel = input("is de kaas geel? ")
if geel == "ja":
    gaten = input("zitten er gaten in? ")
    if gaten == "ja":
        duur = input("is de kaas belachelijk duur? ")
        if duur == "ja":
            print("ja kaas is de Emmenthater ")
        elif duur == "nee":
            print("je kaas is de Leerdammer ")
    elif gaten == "nee":
        steen = input("is de kaas hard als steen? ")
        if steen == "ja":
            print("je kaas is de Parmigiano Reggiano")
        elif steen == "nee":
            print("je kaas is de Goudse Kaas")
elif geel == "nee":
    schimmel = input("Heeft de kaas blauwe schimmel? ")
    if schimmel == "ja":
        korst = input("heeft de kaas korst? ")
        if korst == "ja":
            print("je kaas is de Blue Rochbaron")
        elif korst == "nee":
            print("je kaas is de FOume D'ambert")
    elif schimmel == "nee":
        korst_2 = input("heeft de kaas korst")
        if korst_2 == "ja":
            print("je kaas is de Camembert")
        elif korst_2 == "nee":
            print("je kaas is de Mozzarella")