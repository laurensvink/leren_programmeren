dagen = (
    "Maandag", "Dinsdag", "Woensdag", "Donderdag",
    "Vrijdag", "Zaterdag", "Zondag"
)

# Alle dagen
print("Alle dagen van de week zijn:")
for dag in dagen:
    print("-", dag)
print()

# Weekenddagen
print("De weekenddagen zijn:")
for dag in dagen[5:]:
    print(dag)
print()

# Werkdagen
print("De werkdagen zijn:")
for dag in dagen[:5]:
    print(dag)
print()

# Alle dagen omgekeerd
print("Alle dagen van de week in omgekeerde volgorde zijn:")
for dag in reversed(dagen):
    print( dag)
print()

# Werkdagen omgekeerd
print("De werkdagen in omgekeerde volgorde zijn:")
for dag in reversed(dagen[:5]):
    print("-", dag)
print()

# Weekenddagen omgekeerd
print("De weekenddagen in omgekeerde volgorde zijn:")
for dag in reversed(dagen[5:]):
    print(dag)
    break