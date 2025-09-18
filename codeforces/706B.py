import bisect

n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())

r = []

for _ in range(q):
    m = int(input())
    r.append(bisect.bisect_right(x, m))

print(*r, sep='\n')
