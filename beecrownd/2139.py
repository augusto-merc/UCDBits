months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

r = []

while True:
    try:
        m, d = map(int, input().split())
        if m == 12 and d == 25:
            r.append('E natal!')
        elif m == 12 and d == 24:
            r.append('E vespera de natal!')
        elif m == 12 and d > 25:
            r.append('Ja passou!')
        else:
            r.append(f'Faltam {sum(months[m-1:]) + (25 - d)} dias para o natal!')
        
    except:
        break

print(*r, sep='\n')

