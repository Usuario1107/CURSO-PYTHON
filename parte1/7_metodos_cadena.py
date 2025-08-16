# metodos
# #funcion dir(str) muestra los metodos de la varibale str

cadena1="holaMundo"
cadena2 = "estudiando python"
# print(dir(cadena1))


mayuscula = cadena1.upper()  # convierte a mayusculas
minuscula = cadena1.lower()  # convierte a minusculas

primera_letra_mayuscula = cadena2.capitalize()  # convierte la primera letra a mayuscula
# primera_letra_mayuscula = cadena2.title()  # convierte la primera letra de cada palabra a mayuscula

#busqueda la pocision de caracter conf find(indice)
busqueda_find= cadena1.find("H") # devuelve la posicion del caracter si no lo encuentra devuelve -1
busqueda_find2 = cadena1.find("M")  # devuelve la posicion del caracter si no lo encuentra devuelve -1

#busqueda con index devuelve la posicion del caracter si no lo encuentra devuelve error
busqueda_index = cadena1.index("M")  # devuelve la posicion del caracter si no lo encuentra devuelve error EXEPCION

# IS NUMERIC
es_numero = cadena1.isnumeric()  # devuelve True si la cadena es un numero
# is alpha devuelve True si la cadena es alfabetica
es_alfabetica = cadena1.isalpha()  # devuelve True si la cadena es alfabetica a-z

#count devuelve el numero de veces que se repite un caracter en la cadena
contador = cadena1.count("o")  # devuelve el numero de veces que se repite el caracter o -> tambien puede ser cadena "ndo" o "hola" etc

# funcion len(str) devuelve la longitud de la cadena
longitud = len(cadena1)  # devuelve la longitud de la cadena

# verifica si un cadena empieza con una letra 
cadena = "hola como estas"
empieza_con = cadena.startswith("ola") # devuleve True si empieza con esa letra o cadena 

# tmeins con caracter o subcadena
termina_con = cadena.endswith("estas") #devuelve True si temina con esa cadena o caracter

# reemplazar  una cadena con un subcadena o carcter recibe dos parametros
cadena_nueva = cadena.replace("comoH","H") # remplaza el primer parametro de la cadena "hoola" por H si no encuentra la palabra devuelve la mism cadena

cadena = "hola como esta espero que muy bien"
# METOD  QUE DEVUELVE UN LISTA 

nueva_lista = cadena.split(" ") # devuleve un lista separa por el parametro que le damos ejmplo " " espacion o otro caracter si no encuentra el caracter devuelve la msima cadena
print(nueva_lista)  



