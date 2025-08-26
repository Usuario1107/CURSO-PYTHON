# esto es mas limitado y mucho recurso de consumo
archivo = open("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivotxt\\archivo.txt",encoding="UTF-8") # el , encding = "UTF-8" parametro de codificacion para caracteres universales
# leer_archivo = archivo.read()

leer_lineas = archivo.readlines() # guarda en una lista todas las lineas

archivo.close()
print(leer_lineas[0])
