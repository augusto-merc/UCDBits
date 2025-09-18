n1 = input()
n2 = input()

r = ''.join(['0' if n1[i] == n2[i] else '1' for i in range(len(n1))])

print(r)
