# Controleert of een getal een priemgetal is.
def is_prime(number: int) -> bool:
    # Controleer of het getal kleiner dan of gelijk aan 1 is; dit zijn geen priemgetallen
    if number <= 1:
        return False
    
    # 2 is het eerste priemgetal, dus geef True terug
    if number == 2:
        return True
    
    # Alle even getallen groter dan 2 zijn geen priemgetallen
    if number % 2 == 0:
        return False
    
    # Bereken de maximale deler om te controleren (wortel van number, want grotere delers zijn overbodig)
    max_divisor = int(number**0.5) + 1
    # Controleer alleen oneven delers vanaf 3 tot de maximale deler
    for d in range(3, max_divisor, 2):
        # Als het getal deelbaar is door een deler, is het geen priemgetal
        if number % d == 0:
            return False
    
    # Als geen delers zijn gevonden, is het getal een priemgetal
    return True