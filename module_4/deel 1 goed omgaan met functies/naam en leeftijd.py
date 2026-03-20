def naam_leeftijd():
    name = input("Wat is je naam? ").lower()
    age = int(input("Wat is je leeftijd? "))
    name_age["name"] = name
    name_age["age"] = age

name_age = {}


naam_leeftijd()


values_list = list(name_age.values())
naam = values_list[0] 
leeftijd = values_list[1]  

print(f"je naam is {naam} en je bent {leeftijd} jaar")
