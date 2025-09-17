n = int(input())

r = []

for i in range(n):
    h, d, g = map(int, input().split())

    if (200 <= h <= 300) and (50 <= d) and (150 <= g):
        r.append('Sim')
    else:
        r.append('Nao')

print(*r, sep='\n')
