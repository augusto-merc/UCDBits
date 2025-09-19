n, m = map(int, input().split())

a = [input() for _ in range(m)]

print(n + a.count('fechou') - a.count('clicou'))
