
conjunto = set(["will",24,True])
conjunto = {"will",24,True} # crear sin set
conjunto.add("hola") # agregar un dato
conjunto.add(24) # no agrega porque ya existe el dato
conjunto.remove(24) # eliminar un dato si no existe da error
conjunto.discard(24) # eliminar un dato si no existe no da error
# conjunto.clear() # eliminar todos los datos del conjunto

conjunto_2 = frozenset({"hola",45,False}) # crear un conjunto inmutable no se puede modificar
conjunto_3 = {"es todo",conjunto_2}


print(conjunto)
print(conjunto_2)
