import sys

n = int(sys.stdin.readline().strip())

s = (c for i in sys.stdin.readline().strip().split('b') if (c := len(i)) > 1)
print(sum(s))
