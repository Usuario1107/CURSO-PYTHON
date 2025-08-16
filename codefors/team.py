def es_resuelto(problema):
    count=0
    for valor in problema:
        if valor == 1:
            count +=1
    return True if count>= 2 else False
N = int(input())
problemas = [list(map(int,input().split())) for _ in range(N)]
contador=0
for lista in problemas:
    if es_resuelto(lista):
        contador +=1
print(contador)
