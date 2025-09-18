from math import gcd

a, b, c, d = map(int, input().split())

num = a * d + c * b

den = b * d

g = gcd(num, den)

print(f"{num // g} {den // g}")
