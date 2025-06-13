def dibujar():
    # Leer el número de árboles
    num_arboles = int(input())
    
    # Leer las alturas de los árboles
    alturas = list(map(int, input().split()))
    
    # Calcular la altura máxima de todos 1los árboles
    altura_maxima = max(alturas) if alturas else 0
    
    # Calcular dimensiones de la cuadrícula
    filas = altura_maxima + 2  # +2 para la copa y el tronco
    columnas = 4 * num_arboles + 1  # Cada árbol ocupa 4 columnas + 1 extra
    
    # Crear cuadrícula inicial con puntos
    cuadricula = [['.' for _ in range(columnas)] for __ in range(filas)]
    
    # Construir la línea del tronco (última fila)
    tronco = "__"  # Inicio del tronco
    for i in range(num_arboles):
        tronco += "|"  # Añadir el tronco del árbol actual
        # Añadir separación: "___" entre árboles, "__" al final
        tronco += "___" if i < num_arboles - 1 else "__"
    
    # Colocar el tronco en la última fila de la cuadrícula
    cuadricula[-1] = list(tronco)
    
    # Calcular posiciones centrales de cada árbol
    centros = [2 + 4 * i for i in range(num_arboles)]
    
    # Dibujar cada árbol en la cuadrícula
    for indice in range(num_arboles):
        altura_actual = alturas[indice]
        centro = centros[indice]
        
        # Calcular fila donde comienza la copa
        fila_copa = altura_maxima - altura_actual
        
        # Dibujar la copa del árbol (^)
        cuadricula[fila_copa][centro] = '^'
        
        # Dibujar el cuerpo del árbol (desde debajo de la copa hasta el tronco)
        for fila in range(fila_copa + 1, altura_maxima + 1):
            cuadricula[fila][centro - 1] = '/'   # Rama izquierda
            cuadricula[fila][centro] = '|'        # Tronco central
            cuadricula[fila][centro + 1] = '\\'   # Rama derecha (escapar la barra invertida)
    
    # Imprimir la cuadrícula completa
    for fila in cuadricula:
        print(''.join(fila))

dibujar()