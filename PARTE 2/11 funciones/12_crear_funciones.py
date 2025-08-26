# def nombre_funion(parametros,,,,n):
#      return valor:

# funion basica sin parametros ni retorno
def imprimir_mensaje():
    print("Hola, este es un mensaje de ejemplo")

imprimir_mensaje() 

# funion con parametros
def saludar(nombre = "usuario"): # si no se le pasa parametro se le asigna el valor por defecto de usuario
    saludo = f"hola {nombre} bienvenido al curso de python"
    return saludo

# parametro *args permite recibir un numero indefinido de parametros

def sumar(*variables):
    return sum(variables)

print(saludar("Goku"))
print(saludar("Vegueta"))
print(saludar())

# funion con tipo de datos entrada y salida
def sumar(a: int, b: int) -> int:
    return a + b

print(sumar(3, 5))  # Resultado: 8

print(sumar(1,2,3,4,5,6,7))
print(sumar(10,20))


