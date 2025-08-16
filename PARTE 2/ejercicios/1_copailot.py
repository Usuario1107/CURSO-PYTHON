# El profe no vino a clase y los alumnos se pusieron a hacer la lista.
# 1. Mostrar de mayor a menor los datos.
# 2. El mayor es el profesor y el menor el asistente.

def ordenar_alumnos(alumnos):
    # Usamos sorted() para ordenar por la edad (índice 1) de mayor a menor
    return sorted(alumnos, key=lambda x: x[1], reverse=True)

def mostrar_datos(alumnos):
    print("Lista de alumnos de mayor a menor:")
    for alumno in alumnos:
        print(f"{alumno[0]} {alumno[1]}")
    print(f"El profesor es {alumnos[0][0]}")
    print(f"El asistente es {alumnos[-1][0]}")

# Entrada de datos
n = int(input("Cantidad de alumnos: "))
alumnos = [input(f"Ingrese el nombre y edad del alumno {i + 1}: ").split() for i in range(n)]
alumnos = [[alumno[0], int(alumno[1])] for alumno in alumnos]  # Convertir edad a entero

# Mostrar resultados

[["Ana", ["puntos",6]], ["Juan", ["puntos",66]], ["Luis", ["puntos",45]]]