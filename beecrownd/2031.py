n = int(input())
r = []

for _ in range(n):
    j1 = input()
    j2 = input()
    if j1 == j2 == 'ataque':
        r.append('Aniquilacao mutua\n')
    elif j1 == j2 == 'pedra':
        r.append('Sem ganhador\n')
    elif (j1, j2) in [('ataque', 'pedra'), ('ataque', 'papel'), ('pedra', 'papel')]:
        r.append('Jogador 1 venceu\n')
    elif (j1, j2) in [('pedra', 'ataque'), ('papel', 'ataque'), ('papel', 'pedra')]:
        r.append('Jogador 2 venceu\n')
    else:
        r.append('Ambos venceram\n')

print(''.join(r), end='')
