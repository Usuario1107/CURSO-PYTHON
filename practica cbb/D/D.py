def dibujar():
    num_arboles = int(input())
    
    alturas = list(map(int, input().split()))
    
    altura_maxima = max(alturas) if alturas else 0
    
    filas = altura_maxima + 2  
    columnas = 4 * num_arboles + 1  
    
    cuadricula = [['.' for _ in range(columnas)] for __ in range(filas)]
    
    tronco = "__" 
    for i in range(num_arboles):
        tronco += "|"  

        tronco += "___" if i < num_arboles - 1 else "__"
    
    cuadricula[-1] = list(tronco)
    
    centros = [2 + 4 * i for i in range(num_arboles)]
    
    for indice in range(num_arboles):
        altura_actual = alturas[indice]
        centro = centros[indice]
        
        fila_copa = altura_maxima - altura_actual
        
        cuadricula[fila_copa][centro] = '^'
        
        for fila in range(fila_copa + 1, altura_maxima + 1):
            cuadricula[fila][centro - 1] = '/'   
            cuadricula[fila][centro] = '|'       
            cuadricula[fila][centro + 1] = '\\'  

    for fila in cuadricula:
        print(''.join(fila))

dibujar()