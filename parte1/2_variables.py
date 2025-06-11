nombre = "juan"  #string 
edad = 20        # entero
decimal = 3.5    # flotante
bool = True      #boleano -> True o False 
# ><

#concatenar cadenas
saludo = "hola"
bienbenida = "bienvenido"

print(saludo +" "+ nombre +" "+ bienbenida) #hola juan bienbenido
print(f"{saludo} {nombre} {bienbenida}") # con F -> format string convierte a string las varibles entre llaves ejmeplo un int ..etc

del nombre # eliminar variable 
print(f"{saludo} {decimal} {bienbenida}") # hola 3.5 bienbenido

print("hola" in bienbenida) # True -> si esta la palabra hola en la     variable bienbenida

