import sys

def solve():
    n, _ = map(int, sys.stdin.readline().split())
    
    s = sys.stdin.readline().strip()

    num_restritas = s.count('1')

    contador_pequenos = 1       # Começa em 1 e sobe
    contador_grandes = num_restritas + 1 # Começa no primeiro número grande e sobe

    p = [0] * n
    for i in range(n):
        if s[i] == '1':
            p[i] = contador_pequenos
            contador_pequenos += 1
        else:
            p[i] = contador_grandes
            contador_grandes += 1

    print("YES")
    print(*p)


def main():
    try:
        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()
