def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return b

    c = a % b
    while c != 0:
        a, b = b, c
        c = a % b
    return b


print(gcd(210, 45))
print(gcd(77, 7))
print(gcd(100, 0))
print(gcd(100, 1))
