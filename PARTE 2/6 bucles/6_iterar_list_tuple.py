# esto sirve tanto como lista y como tupla
# las tuplas son inmutables y las listas mutables
# los que etsamos haciendo en ver los valores de una lista y tupla
animales = ("Perro", "Gato", "León", "Tigre", "Elefante")  # Animales
frutas = ["Manzana", "Banana", "Naranja", "Fresa", "Sandía"]     # Frutas
verduras = ["Zanahoria", "Lechuga", "Tomate", "Pepino", "Brócoli"]  # Verduras

#iterar sobnre un lista
for animal in animales:
    print(animal)

# interar sonre dos o mas  listas de misma tamaño al mismo tiempo
for animal, fruta, verdura in zip(animales,frutas,verduras):
    print(f"{animal} - {fruta} - {verdura}")

# iterar numeron en rango:(0 hatsa n-1) aranca de 0 hasta n-1
# rango recibe parametros (inicio, fin, paso) = (0,10,2) saltando dos en dos
for i in range(5):
    print(i)
print("------------------")
for i in range(0,10,2):
    print(i)

print("----------------")
# iterar sobre rango y lista al mismo tiempo
for i,animal in enumerate(animales): # esto es util cuando queremos los elementos y el inidce ygual 
    print(f"{i} : {animal} <=> {animales[i]}")
    if i == 3:
        break # en la  iteracion 3 se sale del bucle y no va entrar al else:
else:
    print("iteracion finalizada") # se ejecuta al final de la iteracion


