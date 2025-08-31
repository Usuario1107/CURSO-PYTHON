import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_archivo = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\graficos\\bigote.csv")

sns.boxplot(x= "Cat",y="Valor",data=df_archivo) # dibujar mostrar

plt.show()# mostrar grafico
