import random

cijfers = [0,1,2,3,4,5,6,7,8,9]
speciale_getallen = ['@', '#', '$', '%', '&', '_', '?']
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alfabet_hoofdletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def passwordgenerator():
    password = []

    for i in range(6):
        password.append(random.choice(cijfers))

    for i in range(3):
        password.append(random.choice(speciale_getallen))

    for i in range(8):
        password.append(random.choice(alfabet))

    for i in range(7):
        password.append(random.choice(alfabet_hoofdletters))

    random.shuffle(password)

    return ''.join(str(x) for x in password)


def test(wachtwoord):
    specials = set('@#$%&_?')
    lower = set('abcdefghijklmnopqrstuvwxyz')

    if len(wachtwoord) != 24:
        return False

    if not (2 <= sum(c.isupper() for c in wachtwoord) <= 6):
        return False

    if sum(c.islower() for c in wachtwoord) < 8:
        return False

    if not (4 <= sum(c.isdigit() for c in wachtwoord) <= 7):
        return False

    if sum(c in specials for c in wachtwoord) != 3:
        return False

    if wachtwoord[11].isupper() or wachtwoord[12].isupper():
        return False

    if wachtwoord[-1] in lower:
        return False

    if wachtwoord[0] in specials or wachtwoord[-1] in specials:
        return False

    if any(c.isdigit() for c in wachtwoord[:3]):
        return False

    return True


for i in range(500):
    ww = passwordgenerator()
    if not test(ww):
        print(ww)