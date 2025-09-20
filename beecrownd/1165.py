def primo(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input())

r = []
for i in range(n):
    x = int(input())
    if primo(x):
        r.append(f'{x} eh primo')
    else:
        r.append(f'{x} nao eh primo')
        
print('\n'.join(r))
