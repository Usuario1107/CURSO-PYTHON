# metodos de listas
lista = list(["hola" ,23 , "como" ,"estas", True]) #con list() util para convertir si es un set o tuplas

longitud = len(lista) # funcion de longitud de lista
lista.append("jajaj") # mosdifica la lista agrega elemento a la lista

lista.insert(6,2456 ) # en el indice 2 actulizar 2456 modifica la lista si no hay el indice lo agrega al final

lista.extend([2,4,5,67]) # agregar una sublista a nuestra lista

lista.pop(5) # eliminar el el elmento  de la lista
lista.pop(-1) #eliminamos el ultimo elemeto de la lista 
lista.pop(-2) # eliminamos el penultimo elemento de lista

# eliminar un eelemnto de la lista por su valor
lista.remove("hola") # si no encuentra el valor devuelve error

#lista.clear() #eliminar los vlaores de la lista

lista_numeros = [4 ,5, 6, 7, 4, 9, 12, 56, 2, 1, 0, -1]
print(lista_numeros)
lista_numeros.sort() # modifica las lista ordena ascendente solo con numeros y boleanos pero son primeros antes que los numeros
print(lista_numeros)
lista_numeros.sort(reverse = True) # ordena descendente

lista_numeros = [4 ,5, 6, 7, 4, 9, 12, 56, 2, 1, 0, -1]
print(lista_numeros)
lista_numeros.reverse() # invierta la lista no ordena nada solo inverte
print(lista_numeros)

indice = lista_numeros.index(56) # devuelve el indice del valor 56 si no encuentra devulve error encepcion y con count() deulve -1
print(indice)
