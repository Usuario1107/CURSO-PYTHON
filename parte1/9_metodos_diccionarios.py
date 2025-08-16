# metodos de diccionario
diccionario = {
    "edad" : 23,
    "nombre" : "will",
    "apellido" : "ballest",
    "dni" : 234566,}

claves = diccionario.keys() #devuleve claves del diccionario
nombre = diccionario.get("nombre")# devuelve el valor de la clave nombre ,si no necuentra devuelve none
edad = diccionario["edad"] # el get si no encuentra devuelve error expepcion

#diccionario.clear() #elimina el diccionario modifica 
diccionario.pop("nombre") #elimina el nombre de mi diccionario modifica 

diccionario.items() #esto sirve para iterar el diccionario

# .values() - devuelve todos los valores del diccionario
valores = diccionario.values()
print("Valores:", valores)

# .update() - actualiza el diccionario con otro diccionario
diccionario.update({"pais": "Perú"})
print("Después de update:", diccionario)

# .setdefault() - obtiene el valor de una clave, si no existe la crea con un valor por defecto
correo = diccionario.setdefault("correo", "sin correo")
print("Correo:", correo)
print("Después de setdefault:", diccionario)

# .popitem() - elimina y devuelve el último par clave-valor insertado
ultimo = diccionario.popitem()
print("Elemento eliminado con popitem:", ultimo)
print("Después de popitem:", diccionario)

print(diccionario)
print(nombre)
print(edad)