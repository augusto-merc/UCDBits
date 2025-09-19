s, t, f = map(int, input().split())

out = s + t + f
if out > 24:
    print(out - 24)
elif out < 0:
    print(out + 24)
else:
    print(out)
