n = int(input())

x = list(map(int, input().split()))

s = sum(x)

i = 0
a = set()
while 0 <= i < n:
    a.add(i)
    temp = -1 if x[i] % 2 == 0 else 1
    if x[i] > 0:
        x[i] -= 1
        s -= 1
    i += temp

print(len(a), s)
