def saber(arr, n, m):
    
    def verificar(arg, row, col):
        for k in range(row-1, row+2):
            for l in range(col-1, col+2):
                if k == row and l == col:
                    continue
                if arg[k][l] != 7:
                    return False
        return True
        ...
    
    
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] == 42:
                if verificar(arr, i, j):
                    return f'{i+1} {j+1}'
    return '0 0'


n, m = map(int, input().split())

wave = [list(map(int, input().split())) for _ in range(n)]

print(saber(wave, n, m))
