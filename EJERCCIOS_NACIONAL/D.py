from itertools import combinations

n, m = map(int, input().split())

combinaciones_explosivas = []
for _ in range(m):
    linea = list(map(int, input().split()))
    k = linea[0]
    elementos = set(linea[1:k+1])
    combinaciones_explosivas.append(elementos)

pociones_validas = 0

for tamaño in range(n + 1):
    for subconjunto in combinations(range(1, n + 1), tamaño):
        conjunto_actual = set(subconjunto)
        
        es_valida = True
        for explosiva in combinaciones_explosivas:
            if explosiva.issubset(conjunto_actual):
                es_valida = False
                break
        
        if es_valida:
            pociones_validas += 1

print(pociones_validas)