import sys

def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline().strip())
if isprime(n):
    print(1)
elif n % 2 == 0:
    print(2)
elif isprime(n - 2):
    print(2)
else:
    print(3)
