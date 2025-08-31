# cmabie tipo de dato de un columna
import pandas as pd

df_notas = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\archivo_csv\\ejercicios_txst_csv\\notas.csv")
# convertir una columna a string
df_notas["Nota1"] = df_notas["Nota1"].astype(str)
# reemplazar un columna los datos por otro 
# df_notas["Estudiante"].replace("Luis","Mondongo",inplace=True) # reemplaze en estudientes a todo lso LUIS por mondongo

#print(type(df_notas["Nota1"][0]))
# ELIMINAR DATOS FALTANTES
df_notas = df_notas.dropna() # elimianr filas axis=0 , columnas = axis=1
# eliminar filas repetidas
df_notas = df_notas.drop_duplicates()

# creando un csv con los actulizados 
df_notas.to_csv("\CURSO DE PYTHON\\PARTE 3(modulos)\\archivo_csv\\ejercicios_txst_csv\\notas_limpio.csv")
print(df_notas)