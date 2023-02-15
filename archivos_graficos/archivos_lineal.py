import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("curso_python\\archivos_graficos\\tweets.csv")

# creando el grafico
sns.lineplot(x="fechas", y="tweet", data=df)
# creando un punto en el maximo
plt.plot("2022-10-28", 12,"o")
#mostrando el grafico
plt.show()