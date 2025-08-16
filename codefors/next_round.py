def proxima_ronda(notas, k):
    aprobados = 0
    for i,nota in enumerate(notas):
        if nota != 0 and i < k:
            aprobados +=1
        elif nota != 0 and i >= k and notas[k-1] == nota :
            aprobados +=1
    return aprobados

n_k=list(map(int,input().split()))
lista = list(map(int,input().split()))

if len(lista) == n_k[0]:
    print(proxima_ronda(lista,n_k[1]))
