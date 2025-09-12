import sys
from math import ceil

output = [(lambda n, k: ceil(n / (k - 1)) if n % 2 == 0 else 1 + ceil((n - k) / (k - 1)))(*map(int, sys.stdin.readline().strip().split())) for _ in range(int(sys.stdin.readline().strip()))]
        
print(*output, sep='\n')
