r = []
while (t := int(input())) != 0:
    for _ in range(t):
        n = int(input())
        r.append((lambda x: (n - x) * 2 + x)(2 if n % 2 == 0 else 1))

print(*r, sep='\n')
