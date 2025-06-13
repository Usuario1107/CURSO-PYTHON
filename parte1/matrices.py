filas = 3
columnas = 4

matriz = []  # Empieza vacía

for i in range(filas):  # Por cada fila
    fila = []           # Creamos una lista vacía para esa fila
    for j in range(columnas):  # Por cada columna
        fila.append(4)    # Agregamos un 1 a la fila
    matriz.append(fila)   # Agregamos la fila completa a la matriz

# Ahora mostramos la matriz
for fila in matriz:
    print(fila)
