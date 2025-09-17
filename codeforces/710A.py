import sys

columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

c, d = [i for i in input()]

c = columns[c]
d = int(d) - 1

match (c, d):
    case (0, 0) | (0, 7) | (7, 0) | (7, 7):
        print(3)
    case (0, _) | (7, _) | (_, 0) | (_, 7):
        print(5)
    case _:
        print(8)
