import sys

n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
l = [int(sys.stdin.readline().strip()) for _ in range(q)]
for i in l:
    if i in a:
        print(a.index(i))
    else:
        print(-1)
