import pandas as pd

archivo = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivo_csv\\archivo.csv")

fechas = archivo["Fecha"]

print(archivo)
print("---------------------------------------------------------------------")
# ordenar el csv por un inidice
datos_ordenado_temp = archivo.sort_values("Sensor_Temperatura") # ordenar por la clave de sensor
datos_ordenados_descen_hora = archivo.sort_values("Hora",ascending=False)
""" # concatenar do archivos
archivo_2 = []
archivos_unido = pd.concat([archivo,archivo_2]) #metodo contac pide un lista con todo los datos a concatenar """

#acceder a la pimer fila
primera_fila = archivo.head(1) # acceder a filas  de primero al ultimo [0] son indices de los valores
ultima_fila = archivo.tail(1) # de ultimo hacia primero

#saber el tamaño de elementos del archivo
fila,columna = archivo.shape #es atributo 
# obteniendo datos estadistcos del archivo con describe()
datos_esta = archivo.describe()
# acceder a un elemento del archivo con loc[#fila,"name_columna"]
elemento_loc = archivo.loc[2,"Hora"]
#acceder  a elemno pir indice iloc[x,y]
elemento_iloc = archivo.iloc[1,2] # fila y columna
# accediendo a todas las filas de un columna 
Horas = archivo.iloc[:,1] # acceder a horas todo los valores de esa columna
segunda_filas = archivo.iloc[1,:] # acceder a los valores de la fina 1 hasta con su nombre de columna
filas_humedad_mayores_40 = archivo.loc[archivo["Sensor_Humedad"] > 40,:] # con loc porque permite poner en nombre de la columas
print(filas_humedad_mayores_40)

