from functions import *
from test_lib import test, report

expected = False # is -7 een priemgetal? nee dus false
result = is_prime(-7)
test('TEST: is_prime(-7)',expected, result)

expected = False # is 0 een priemgetal? nee dus false
result = is_prime(0)
test('TEST: is_prime(0)',expected, result)

expected = False # is 1 een priemgetal? nee dus false
result = is_prime(1)
test('TEST: is_prime(1)',expected, result)

expected = True # is 2 een priemgetal? ja dus true
result = is_prime(2)
test('TEST: is_prime(2)',expected, result)

expected = True # is 7 een priemgetal? ja dus true
result = is_prime(7)
test('TEST: is_prime(7)',expected, result)

expected = False # is 66 een priemgetal? nee dus false
result = is_prime(66)
test('TEST: is_prime(66)',expected, result)

expected = True # is 101 een priemgetal? ja dus true
result = is_prime(101)
test('TEST: is_prime(101)',expected, result)

expected = False # is 19872496 een priemgetal? nee dus false
result = is_prime(19872496)
test('TEST: is_prime(19872496)',expected, result)

if __name__ == "__main__":
    report()
