import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_archivo = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\graficos\\barras.csv")

sns.barplot(x= "Categoria",y="Valor",data=df_archivo) # dibujar mostrar
total_datos = df_archivo["Valor"].sum()
print(total_datos)
plt.show()# mostrar grafico
