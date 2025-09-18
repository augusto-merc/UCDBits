m = input().split()

r = [''.join([m[i][j] for j in range(len(m[i])) if j % 2 != 0]) for i in range(len(m))]
    
print(' '.join(r))
