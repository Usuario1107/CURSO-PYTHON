from bisect import bisect_right
from itertools import combinations

n, t = map(int, input().split())
tiempos = list(map(int, input().split()))

def posibles_sumas(lista):
    res = []
    for i in range(len(lista)+1):
        for comb in combinations(lista, i):
            total = sum(comb)
            if total <= t:
                res.append(total)
    return res

mitad = n // 2
izq = tiempos[:mitad]
der = tiempos[mitad:]

suma_izq = posibles_sumas(izq)
suma_der = posibles_sumas(der)

suma_der.sort()
mejor = 0

for s in suma_izq:
    falta = t - s
    idx = bisect_right(suma_der, falta)
    if idx > 0:
        total = s + suma_der[idx-1]
        if total > mejor:
            mejor = total

print(mejor)
