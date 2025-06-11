#condicionales 
# if, elif, else
# Ejemplo 1: Condicional simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")  # Se ejecuta si la condición es verdadera
else:
    print("Eres menor de edad")

# Ejemplo 2: Condicional con elif
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Bueno")
elif nota >= 60:
    print("Regular")
else:
    print("Insuficiente")
# Ejemplo 3: Condicional anidado
numero = 10
if numero > 0:
    print("El número es positivo")
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

# Ejemplo 4: Condicional con operadores lógicos
edad = 20
pais = "España"
if edad >= 18 and pais == "España":
    print("Eres mayor de edad y estás en España")
# Ejemplo 5: Condicional con operadores lógicos OR
elif edad > 18 or pais != "España":
    print("eres mayor de edad pero no estas en españa")
if edad < 18 or pais != "España":
    print("Eres menor de edad o no estás en España")

# Ejemplo 6: Condicional con operadores lógicos NOT
if not (edad < 18): # true si edad es mayor de 18 
    print("No eres menor de edad")
else:
    print("eres mayor de edad")

# Ejemplo 7: Condicional con operadores de pertenencia
colores = ["rojo", "verde", "azul"]
if "rojo" in colores:
    print("El color rojo está en la lista")
else:
    print("el rojo no esta en la laista")

# Ejemplo 8: Condicional con operadores de pertenencia NOT IN
if "amarillo" not in colores:
    print("El color amarillo no está en la lista")
else:
    print("el amrrilo esta en l alista")




