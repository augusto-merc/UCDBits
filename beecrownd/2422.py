n = int(input())

c = [int(input()) for _ in range(n)]

k = int(input())

l = 0
r = n - 1

while l <= r:
    if (s := c[l] + c[r]) == k:
        print(f'{c[l]} {c[r]}')
        break
    elif s < k:
        l += 1
    else:
        r -= 1
