# se pasa el parametro "w" write
# estoy escribiendo dobre la direccion si no encuentra creara uno si no  lo sobre escrbe
with open("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivotxt\\archivo.txt","w",encoding="UTF-8") as archivo:
    archivo.write("-nombre: daniel \n-edad :23 \n-deporte: padel\n")
    archivo.write("-nombre: Juan \n-edad :13 \n-deporte: pin pon")
    