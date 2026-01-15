dagen = ( 
    "Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"
)
print("alle dagen van de week zijn:")
for dag in dagen:
    print("-", dag)
print()
for dag in dagen:
    print("de weekenddagen zijn: Zaterdag en Zondag")
print()

print("de werkdagen zijn: Maandag, Dinsdag, Woensdag, Donderdag en Vrijdag")
print()

print("Alle dagen van de week in omgekeerde volgorde zijn:")
print("zondag -> zaterdag -> vrijdag -> donderdag -> woensdag -> dinsdag -> maandag.")
print()

print("De werkdagen in omgekeerde volgorde zijn:")
for dag in reversed(dagen[:5]):
    print("-", dag)

print()
 
print("De weekenddagen in omgekeerde volgorde zijn: zondag + zaterdag.")