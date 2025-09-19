
pi = 3.14
out = []
while True:
    try:
        v = float(input())
        d = float(input())
        r = d / 2
        out.append(f'ALTURA = {v/(pi * (r ** 2)):.2f}\nAREA = {pi * (r ** 2):.2f}')
    except:
        break

print(*out, sep='\n')
