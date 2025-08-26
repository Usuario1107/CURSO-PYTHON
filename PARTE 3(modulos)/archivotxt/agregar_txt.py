# se pasa el parametro "a" append
with open("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivotxt\\archivo.txt","a",encoding="UTF-8") as archivo:
    for i in range(4): # agregar lineas 
        archivo.write(f"\nlinea {i} agregado")