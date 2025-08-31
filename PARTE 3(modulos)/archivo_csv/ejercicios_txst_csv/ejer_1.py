# dos listas con nombre y apellido ,escribir los datos en un archivo de texto de forma optima

nombres = ["alex", "julia", "Daniel"]
apellidos = ["Zamora", "Callizaya", "Zuares"]

with open("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivo_csv\\ejercicios_txst_csv\\datos.txt","w") as archivo:
    [archivo.write(f"nombre: {n} {a} \n\n") for n,a in zip(nombres,apellidos)]
