mtz = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    if 1 in mtz[i]:
        j = mtz[i].index(1)
        movimientos = abs(i - 2) + abs(j - 2)
        break

print(movimientos)
