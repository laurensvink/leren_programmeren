def fibonacci(n):
    reeks = []
    a, b = 0, 1
    for _ in range(n):
        reeks.append(a)
        a, b = b, a + b
    return reeks

# voorbeeld
print(fibonacci(10))