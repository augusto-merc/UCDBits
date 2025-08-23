def star(n, x, i=0, c=0, d=[]):
    if i < 0 or i > n-1 or x[i] == 0:
        return (len(d), c)
    
    if x[i] % 2 != 0:
        x[i] -= 1
        if i not in d:
            d.append(i)
        return star(n, x, i+1, c+1, d)
    
    x[i] -= 1
    if i not in d:
        d.append(i)
    return star(n, x, i-1, c+1, d)
    ...

n = int(input())

x = [int(_) for _ in input().split()]
s = sum(x)

r = star(n, x)

print(r[0], s - r[1])
