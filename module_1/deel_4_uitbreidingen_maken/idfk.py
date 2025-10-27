def kaas():
    if recht_links == "links" and prog_cons == "progressief":
        print("PvdA")
    elif recht_links == "links" and prog_cons == "conservatief":
        print("CU")
    elif recht_links == "rechts" and prog_cons == "progressief":
        print("sgp") 
    elif recht_links == "rechts" and prog_cons == "conservatief":
        print("VVD") 

recht_links = input("Bent u links of rechts? ")
prog_cons = input("Progressief of conservatief? ")
kaas()