import csv

with open("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivo_csv\\archivo.csv",encoding="UTF-8") as archivo:
    leer = csv.reader(archivo)
    for dato in leer:
        print(dato)

