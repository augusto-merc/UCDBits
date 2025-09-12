import sys

n = int(sys.stdin.readline().strip())

s = sum(map(int, sys.stdin.readline().strip().split()))

print(int((5*n - s)/(5 - s/n)))
