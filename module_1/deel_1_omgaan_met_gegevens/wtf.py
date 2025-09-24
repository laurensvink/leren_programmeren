naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
gender = input("Ben je een A) een jonge of B) een meisje? ").lower()
kleur = input("Wat is je favoriete kleur? ")
getal = int(input("Wat is je favoriete getal? "))
verschil = abs(leeftijd-getal)
chose_gender = 'haar' if gender == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{chose_gender.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", kleur)
print(f"Het verschil tussen {chose_gender} leeftijd en {getal} is:", verschil)