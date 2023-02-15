import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("curso_python\\archivos_graficos\\ingresos.csv")

# creando el grafico
sns.barplot(x="fuente", y="ingresos", data=df)
total_ingresos = df["ingresos"].sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos}")
#mostrando el grafico
plt.show()