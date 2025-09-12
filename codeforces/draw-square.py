t = int(input())

result = []
for _ in range(t):
    l, r, d, u = map(int, input().split())
    
    if l == r == d == u:
        result.append('YES')
    else:
        result.append('NO')

print('\n'.join(result))
