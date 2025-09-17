import sys

def sortProblem():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        yield sorted(map(int, sys.stdin.readline().strip().split()))

for r in sortProblem():
    print(*r, sep=' ')
