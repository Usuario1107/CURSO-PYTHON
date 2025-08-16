import heapq

def resolver():
    n, m, k = map(int, input().split())
    
    grafo = {i: [] for i in range(1, n+1)}
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        grafo[u].append((v, w))
        grafo[v].append((u, w))
    
    distancia_minima = camino(grafo, 1, n)
    
    if distancia_minima <= k:
        print("SI")
    else:
        print("NO")

def camino(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]
    
    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
        
        if nodo_actual == destino:
            return dist_actual
            
        if dist_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo[nodo_actual]:
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))
    
    return float('inf')

resolver()