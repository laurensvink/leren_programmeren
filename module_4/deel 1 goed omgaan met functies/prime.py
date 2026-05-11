from functions import *
from test_lib import test, report

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def primes_up_to(n):
    # Geeft alle priemgetallen t/m n
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def first_n_primes(n):
    # Geeft de eerste n priemgetallen
    primes = []
    number = 2

    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1

    return primes


def primes_between(a, b):
    # Geeft alle priemgetallen tussen a en b (inclusief)
    primes = []

    start = min(a, b)
    end = max(a, b)

    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)

    return primes