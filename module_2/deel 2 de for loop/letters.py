tekst = "Hallo Wereld!"
vorig_teken = None


for teken in tekst:
    if teken != vorig_teken:
        print(teken)
    vorig_teken = teken
