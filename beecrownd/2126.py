r = []
while True:
    try:
        n1 = int(input())
        n2 = int(input())
        
        n1 = str(n1)
        n2 = str(n2)
        
        if n1 in n2:
            r.append((n2.count(n1), n2.rindex(n1) + 1))
        else:
            r.append((0, 0))
    except EOFError:
        break


for i in range(len(r)):

    print(f'Caso #{i + 1}:')
    
    if r[i][0] == 0:
        print('Nao existe subsequencia')
    else:
        print(f'Qtd.Subsequencias: {r[i][0]}')
        print(f'Pos: {r[i][1]}')

    print()

