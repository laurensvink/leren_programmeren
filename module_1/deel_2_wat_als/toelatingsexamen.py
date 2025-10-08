leeftijd = 13
heeft_magische_brief = True
magisch_huisdier = "uil" 
kent_spreuk = True
heeft_stok = True
op_zwarte_lijst = False
geslaagd_aanlegtest = True
heeft_strafblad = False


if leeftijd <11 :
    print("je voldoet niet aan de eisen ")
elif heeft_magische_brief ==  False :
    print("je voldoet niet aan de eisen ")
elif magisch_huisdier not in ["uil", "pad", "kat"]:
    print("Je voldoet niet aan de eisen.")
elif kent_spreuk == False :
    print("je voldoet niet aan de eisen")
elif heeft_stok == False :
    print("je voldoet niet aan de eisen")
elif op_zwarte_lijst == True :
    print("je voldoet niet aan de eisen")
elif geslaagd_aanlegtest == False :
    print("je voldoet niet aan de eisen")
elif heeft_strafblad == True :
    print("je voldoet niet aan de eisen")
else :
    print("je bent toegelaten!")

