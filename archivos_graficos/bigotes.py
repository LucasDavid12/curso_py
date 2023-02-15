import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

df = pd.read_csv("curso_python\\archivos_graficos\\bigotes.csv")
df1 = pd.read_excel("curso_python\\archivos_graficos\\Venezuela-sub21.xlsx")
print(df1)
# creando el grafico
#sns.boxplot(x="categoria", y="valor", data=df)

#mostrando el grafico
#plt.show()