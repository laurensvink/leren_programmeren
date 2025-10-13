import random

num1 = random.randint(1, 10)
num2 = random.randint(5, 15)
answer = input(f'Weet jij wat {num1} + {num2} is? ')

try:
    if int(answer) == num1 + num2:
        print('Dat is juist!')
    else:
        print('Nee, dat klopt niet.')
except:
    print('Dat is geen geldig nummer!')
        