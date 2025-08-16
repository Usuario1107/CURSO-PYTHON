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

print(saludar("Goku"))
print(saludar("Vegueta"))
print(saludar())


