# Crear una lista
lista = [1, 2, 3, 4, 5]
lista_vacia = []  # Lista vacía
# ------------------------------
# Añadir elementos
# ------------------------------
lista.append(6)  # Agrega un solo elemento al final
lista.insert(2, 99)  # Inserta 99 en la posición 2
lista.extend([7, 8, 9])  # Agrega varios elementos al final
# ------------------------------
# Eliminar elementos
# ------------------------------
lista.remove(99)  # Elimina el valor 99 (si existe)
# lista.remove(123)  # Error si 123 no está en la lista (ValueError)
ultimo = lista.pop()  # Elimina el último y lo guarda
tercero = lista.pop(2)  # Elimina el elemento en la posición 2
# lista.pop(100)  # Error si el índice no existe (IndexError)
del lista[0]  # Elimina el elemento en la posición 0
lista.clear()  # Elimina todos los elementos
# ------------------------------
# Buscar y contar
# ------------------------------
lista = [10, 20, 30, 20, 40, 50]
print(20 in lista)  # True
print(lista.index(20))  # Devuelve el índice de la primera aparición
# print(lista.index(999))  # Error si el valor no está (ValueError)
print(lista.count(20))  # Cuántas veces aparece 20
# -----------------------------
# Ordenar y revertir
# ------------------------------
lista.sort()  # Ordena ascendente
lista.sort(reverse=True)  # Ordena descendente
lista.reverse()  # Invierte el orden actual
ordenada = sorted(lista)  # Crea una nueva lista ordenada
inversa = list(reversed(lista))  # Nueva lista invertida
# ------------------------------
# Copiar y cortar (slicing)
# ------------------------------
copia = lista.copy()
sublista = lista[1:4]  # Elementos del índice 1 al 3
# ------------------------------
# Funciones útiles
# ------------------------------
print(len(lista))  # Cantidad de elementos
print(sum(lista))  # Suma (solo si son números)
print(max(lista))  # Valor máximo
print(min(lista))  # Valor mínimo
# ------------------------------
# Recorrer listas
# -----------------------------
for x in lista:
    print(x)
for i, x in enumerate(lista):
    print(f"Posición {i}, valor {x}")
# ------------------------------
# Comprensiones de lista
# ------------------------------
lista = [1, 2, 3, 4, 5, 6]
pares = [x for x in lista if x % 2 == 0]
cuadrados = [x**2 for x in lista]
# ------------------------------
# Técnicas útiles en competencias
# ------------------------------
# Eliminar todos los que cumplan una condición (por ejemplo, eliminar 2)
lista = [1, 2, 3, 2, 4, 2, 5]
lista = [x for x in lista if x != 2]
# Eliminar duplicados conservando orden
lista = [1, 2, 2, 3, 1, 4]
sin_duplicados = []
vistos = set()
for x in lista:
    if x not in vistos:
        sin_duplicados.append(x)
        vistos.add(x)
# ------------------------------
# Convertir entre estructuras
# -----------------------------
conjunto = set(lista)  # Elimina duplicados, sin orden
lista_desde_conjunto = list(conjunto)
tupla = tuple(lista)  # Lista a tupla
# ------------------------------
# Manejo de errores común
# ------------------------------
try:
    print(lista.index(999))
except ValueError:
    print("Valor no encontrado en la lista")
try:
    print(lista.pop(100))
except IndexError:
    print("Posición fuera de rango")

