n = int(input())

h = list(map(int, input().split()))

temp1 = [((h[i] < h[i + 1]), (h[i] > h[i + 1])) for i in range(n - 1)]

if (l := len(temp1)) == 1 and temp1[0][0] == temp1[0][1]:
    print(0)
elif l == 1 and temp1[0][0] != temp1[0][1]:
    print(1)
else:
    for i in range(l - 1):
        if (temp1[i][0] == temp1[i + 1][0]) or (temp1[i][1] == temp1[i + 1][1]):
            print(0)
            break
    else:
        print(1)
