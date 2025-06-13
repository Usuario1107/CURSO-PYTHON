import heapq

N_M = list(map(int, input().split()))
N, M = N_M[0], N_M[1]


grafo = [[] for _ in range(N + 1)]


for _ in range(M):
    inicio, fin, peso = map(int, input().split())
    grafo[inicio].append((fin, peso))

k = int(input())


origen = 1
destino = N

cola = []

heapq.heappush(cola, (0, origen, [origen]))


caminos_encontrados = 0

while cola:
    costo_actual, nodo_actual, camino = heapq.heappop(cola)
    

    if nodo_actual == destino:
        caminos_encontrados += 1
   
        if caminos_encontrados == k:
            print(costo_actual)
            break
  
        continue
    
   
    for vecino, peso in grafo[nodo_actual]:
      
        if vecino not in camino:
            nuevo_costo = costo_actual + peso
            nuevo_camino = camino + [vecino]
            heapq.heappush(cola, (nuevo_costo, vecino, nuevo_camino))
else:
    
    print(-1)
