from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')

# -------- INPUT --------
nr_persons = input_nr_persons("Aantal personen: ")

# ----- CALCULATIONS ----
factor = nr_persons / RECIPE_PERSONS

amount_eggs = round_piece(AMOUNT_EGGS * factor)
amount_milk = round_quarter(AMOUNT_MILK * factor)
amount_salt = round_quarter(AMOUNT_SALT * factor)
amount_pepper = round_quarter(AMOUNT_PEPPER * factor)
amount_oil = round_quarter(AMOUNT_OIL * factor)
amount_onions = round_piece(AMOUNT_ONIONS * factor)
amount_garlics = round_piece(AMOUNT_GARLICS * factor)
amount_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)
amount_spinach = round_quarter(AMOUNT_SPINACH * factor)
amount_cheese = round_quarter(AMOUNT_CHEESE * factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')

print(f'{amount_eggs} {UNIT_PIECES} {TXT_EGGS}')
print(f'{amount_milk} {UNIT_CUPS} {TXT_MILK}')
print(f'{amount_salt} {UNIT_TEASPOONS} {TXT_SALT}')
print(f'{amount_pepper} {UNIT_TEASPOONS} {TXT_PEPPER}')
print(f'{amount_oil} {UNIT_SPOONS} {TXT_OIL}')
print(f'{amount_onions} {UNIT_PIECES} {TXT_ONIONS}')
print(f'{amount_garlics} {UNIT_PIECES} {TXT_GARLICS}')
print(f'{amount_paprikas} {UNIT_PIECES} {TXT_PAPRIKAS}')
print(f'{amount_spinach} {UNIT_CUPS} {TXT_SPINACH}')
print(f'{amount_cheese} {UNIT_CUPS} {TXT_CHEESE}')

print('-----------------------------------------------')