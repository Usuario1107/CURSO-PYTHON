def resolver():
    n, k = map(int, input().split())
    votos = list(map(int, input().split()))
    
    suma_total = sum(votos)
    
    residuo_suma = suma_total % k
    
    contador = 0
    for voto in votos:
        if voto % k == residuo_suma:
            contador += 1
    
    print(contador)

resolver()