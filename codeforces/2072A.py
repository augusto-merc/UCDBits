import sys
from math import ceil

t = int(sys.stdin.readline())
output = []
for i in range(t):
    n, k, p = map(int, sys.stdin.readline().split())
    
    k = abs(k)
    if (v := ceil(k/p)) > n:
        output.append(-1)
    else:
        output.append(v)

print(*output, sep='\n')
