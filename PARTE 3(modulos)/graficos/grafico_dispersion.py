import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_archivo = pd.read_csv("\\CURSO DE PYTHON\\PARTE 3(modulos)\\graficos\\dispersion.csv")

sns.scatterplot(x= "X",y="Y",data=df_archivo) # dibujar mostrar


plt.show()# mostrar grafico
