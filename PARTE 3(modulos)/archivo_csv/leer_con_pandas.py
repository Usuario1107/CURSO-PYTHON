import pandas as pd

archivo = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivo_csv\\archivo.csv")

fechas = archivo["Fecha"]

print(archivo["Estado_Bomba"])

cadena = "0123456789"
print(cadena[0:9:2])
print(cadena[0:4])