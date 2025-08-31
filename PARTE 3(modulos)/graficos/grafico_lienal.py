import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_archivo = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\graficos\\lineal.csv")

sns.lineplot(x= "Fecha",y="Valor",data=df_archivo) # dibujar mostrar
plt.plot("2025-08-06",170,"o") # crear un punto en esa corrdenada
plt.show()# mostrar grafico

print(df_archivo)