# listas o vecotres [] son datos compuestos que pueden contener varios tipos de datos
lista=["texto" , 5 , 4.56 , True]# un alista con str int float y bool la separacion es con comas

print(lista) # ['texto', 5, 4.56, True]
print(lista[2]) # 4.56

#tupla () son datos compuestos que no se pueden modificar
tupla = ("texto" , 5 , 4.56 , True) # una tupla con str int float y bool la separacion es con comas
print(tupla) # ('texto', 5, 4.56, True)
print(tupla[2]) # 4.56 

# tupla[2]=4.56 # TypeError: no puedo modificar una tupla


#set o conjuntos {} son datos compuestos que no se pueden modificar y no tienen orden y se redefine como las tuplas y nos me meustran por indice (si con bucle) y tampoco permite datos duplicados no mostrara los duplicados
conjunto = {"texto" , 5 , 4.56 , True} # un conjunto con str int float y bool la separacion es con comas
print(conjunto)

# diccionario {} son datos compuestos que tienen una clave y un valor
diccionario = {"nombre": "juan",
                "edad": 20,
                "decimal": 3.5,
                "bool": True} # donde tine un clave y un valor como un json
print(diccionario) # {'nombre': 'juan', 'edad': 20, 'decimal': 3.5, 'bool': True}
print(diccionario["edad"]) # edad=20 es como [1] = 1 clave y valor
# print(diccionario[1]) # KeyError: '1' -> no se puede acceder por indice si no por clave


