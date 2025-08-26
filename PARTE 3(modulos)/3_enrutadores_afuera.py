# sirve para importar modulos desde afuera y los que tiene python 
import sys

print(sys.builtin_module_names) # para ver los modulos que tiene python
print(sys.path) # para ver  la ruta de los modulos de python podemos poner nuestro modulos de nosotros

sys.path.append("d:\\CURSO DE PYTHON\\PRUEBA_MODULOS") # agregar solo para este proyecto modulos de PARTE 2 de la carpeta de 11 funiones
print(sys.path)

print("------------------------------------")
import saludo # accediendo afuera hacia saludo.py
saludo.funcion_saludar() 
import carpeta1.despedida as adios # accediendo afura hacia la carpeta de parte1 a despedida.py
adios.despedir()

print("------------------------------------")
# accedamos hacia la parte 2 de funiones 
sys.path.append("d:\\CURSO DE PYTHON\\PARTE 2\\11 funciones")

import funcion  # importamos el modulo saludo
# import 12_crear_funciones  tengo un archivo con numero y esto no es posible definir bien nombre de los archivos
funcion.welcome()
funcion.adios()

from mod_suma import Dos_numeros # importan solo una propiedad de mod_suma.py desde la PARTE 2
Dos_numeros()
