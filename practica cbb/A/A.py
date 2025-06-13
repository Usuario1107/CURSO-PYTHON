import sys
sys.setrecursionlimit(10000)  # Aumentar límite de recursión si es necesario

MOD = 10**9 + 7
memo = {}  # Diccionario para guardar resultados C(x, y)

def C(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    if (x, y) in memo:
        return memo[(x, y)]
    
    # C(x, y) = 2 * sum_{i = x+1 to y} C(i, y)
    total = 0
    for i in range(x+1, y+1):
        total = (total + C(i, y)) % MOD
    result = (2 * total) % MOD
    memo[(x, y)] = result
    return result

# Lectura de entrada
Q = int(input())
for _ in range(Q):
    x1, x2, y1, y2 = map(int, input().split())
    
    # Normalizamos el rectángulo
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)

    total = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            total = (total + C(x, y)) % MOD
    print(total)
