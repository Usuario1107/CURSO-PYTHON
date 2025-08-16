# Crear una matriz vacía de 3x3 (con ceros)
filas, columnas = 3, 3
matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
# Crear matriz 3x3 con un mismo valor
valor = 7
matriz_constante = [[valor] * columnas for _ in range(filas)]
# Crear una matriz identidad de 4x4
n = 4
identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# ------------------------------
# Acceso y modificación
# ------------------------------
# Acceder al elemento (fila 1, columna 2)
print(matriz[1][2])
# Modificar un elemento
matriz[0][1] = 9
# ------------------------------
# Recorrer matriz
# ------------------------------
for fila in matriz:
    print(fila)
for i in range(filas):
    for j in range(columnas):
        print(f"Elemento [{i}][{j}] = {matriz[i][j]}")
# ------------------------------
# Transponer una matriz
# ------------------------------
transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
# ------------------------------
# Rotar matriz 90 grados (horario)
# ------------------------------
# Paso 1: Transponer
# Paso 2: Invertir cada fila
rotada_90 = [list(reversed(col)) for col in zip(*matriz)]
# ------------------------------
# Ordenar filas o columnas
# ------------------------------
# Ordenar cada fila de menor a mayor
matriz_ordenada_filas = [sorted(fila) for fila in matriz]
# Ordenar cada fila de mayor a menor
matriz_ordenada_filas_desc = [sorted(fila, reverse=True) for fila in matriz]
# Ordenar por columna (por ejemplo, columna 0)
matriz_ordenada_col0 = sorted(matriz, key=lambda x: x[0])
# ------------------------------
# Sumar filas y columnas
# ------------------------------
# Suma de la fila 0
suma_fila0 = sum(matriz[0])
# Suma de la columna 1
suma_columna1 = sum(fila[1] for fila in matriz)
# ------------------------------
# Colorear matriz (cambiar valores según condición)
# ------------------------------
# Reemplazar todos los ceros con -1
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] == 0:
            matriz[i][j] = -1
# ------------------------------
# Matriz diagonal (no identidad)
# ------------------------------
diagonal = [[5 if i == j else 0 for j in range(n)] for i in range(n)]
# ------------------------------
# Verificar simetría (matriz igual a su transpuesta)
# ------------------------------
es_simetrica = matriz == transpuesta
# ------------------------------
# Multiplicar escalar a toda la matriz
# ------------------------------
escalar = 3
matriz_escalada = [[x * escalar for x in fila] for fila in matriz]
# ------------------------------
# Manejo de errores comunes
# ------------------------------
try:
    valor = matriz[10][5]  # Acceso fuera de rango
except IndexError:
    print("Índice fuera de la matriz")

