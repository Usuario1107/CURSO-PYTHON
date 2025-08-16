# Crear diccionarios
persona = {"nombre": "Ana", "edad": 30}
vacio = {}  # Diccionario vacío
# ------------------------------
# Añadir y actualizar elementos
# ------------------------------
persona["ciudad"] = "Cochabamba"  # Añadir nueva clave
persona["edad"] = 31  # Actualizar valor existente
# Método update: agrega o actualiza múltiples pares clave-valor
persona.update({"altura": 1.65, "nombre": "Ana María"})
# ------------------------------
# Acceder a elementos
# ------------------------------
print(persona["nombre"])  # Accede al valor por la clave
# print(persona["telefono"])  # Error si la clave no existe (KeyError)
# Acceso seguro con get
print(persona.get("telefono"))  # Devuelve None si no existe
print(persona.get("telefono", "No registrado"))  # Valor por defecto
# ------------------------------
# Eliminar elementos
# ------------------------------
persona.pop("altura")  # Elimina y devuelve el valor asociado
# persona.pop("altura")  # Error si ya fue eliminado (KeyError)
valor = persona.pop("altura", "No encontrado")  # Seguro con valor por defecto
# Eliminar la última clave insertada (desde Python 3.7+)
persona.popitem()  # Elimina y devuelve un (clave, valor) del final
# Eliminar una clave directamente
del persona["ciudad"]
# del persona["ciudad"]  # Error si ya fue eliminada
# Vaciar todo el diccionario
persona.clear()
# ------------------------------
# Claves, valores e ítems
# ------------------------------
datos = {"a": 1, "b": 2, "c": 3}
print(datos.keys())      # dict_keys(['a', 'b', 'c'])
print(datos.values())    # dict_values([1, 2, 3])
print(datos.items())     # dict_items([('a', 1), ('b', 2), ('c', 3)])
# Convertir a listas
claves = list(datos.keys())
valores = list(datos.values())
pares = list(datos.items())
# ------------------------------
# Recorrer diccionarios
# ------------------------------
for clave in datos:
    print(clave, datos[clave])  # Acceso por clave

for clave, valor in datos.items():
    print(f"{clave} => {valor}")
# ------------------------------
# Comprobaciones
# ------------------------------
print("a" in datos)       # True si la clave existe
print("z" not in datos)   # True si la clave no existe
# ------------------------------
# Diccionario por comprensión
# ------------------------------
cuadrados = {x: x*x for x in range(5)}
#------------------------------
# Contar frecuencias (muy útil en competencias)
# ------------------------------
texto = "abracadabra"
frecuencia = {}
for letra in texto:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1
print(frecuencia)
# Alternativa con collections (requiere importación)
# from collections import Counter
# frecuencia = Counter(texto)
# ------------------------------
# Manejo de errores comunes
# ------------------------------
try:
    valor = datos["z"]
except KeyError:
    print("Clave no encontrada")