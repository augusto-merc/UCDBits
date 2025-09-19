t = int(input())

r = ''

for _ in range(t):
    h, m, o = map(int, input().split())
    
    h = '0' + str(h)
    h = h[-2:]
    m = '0' + str(m)
    m = m[-2:]
    
    if o == 0:
        r += f'{h}:{m} - A porta fechou!\n'
    else:
        r += f'{h}:{m} - A porta abriu!\n'

print(r, end='')
