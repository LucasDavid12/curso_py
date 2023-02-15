import pandas as pd
df = pd.read_csv("curso_python\\resolviendo_problemas\\datos.csv")
df["edad"] = df["edad"].astype(str) #convirtiendo un dato numerico a string
df["nombre"].replace("lucas", "Lucas", inplace=True) # reemplazando los datos por otros
df = df.dropna() #elimina datos en filas faltantes (los famossos NA)
df = df.dropna(axis=1) #eliminar datos de columnas faltantes
df= df.drop_duplicates()

# creando un csv con los datos resultantes
df.to_csv("curso_python\\resolviendo_problemas\\datos_nuevos.csv")