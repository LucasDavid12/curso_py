import pandas as pd
# si queremos cargar con nombres de columas especificas es al lado de la ruta -> ", names=["names", "lastname", "age"]"
df = pd.read_csv("curso_python\\archivos\\datos.csv")
df2 = pd.read_csv("curso_python\\archivos\\datos.csv")
nombre = df["nombre"]

# cadena = "0123456789"
# print(cadena[0:5]) buscamos del parametro 0 al 5

# ORDENANDO DE MENOR A MAYOR EL DATA FRAME CON EDAD
df_ordenado = df.sort_values("edad")

# ORDENANDO DE MAYOR A MENOR EL DATA FRAME CON EDAD
df_ordenado = df.sort_values("edad", ascending=False)

# CONCATENAR DOS DATA FRAME
df_concatenado = pd.concat([df, df2])

# VEMOS LAS PRIMERAS FILAS
fila_1 = df.head(2)

# VEMOS LAS ULTIMAS FILAS
ultimas_filas = df.tail(3)

# VEMOS LA CANTIDAD DE FILAS Y COLUMNAS CON SHAPE
filas_y_columas_totales = df.shape

# OBTENIENDO DATA ESTADISTICA DEL DATA FRAME
df_info = df.describe()

# OBTENIENDO UN ELEMENTO ESPECIFICO 
elemento_especifico = df.loc[2, "edad"]

elemento_especifico = df.iloc[2, 2] #solamente con el indice

apellidos = df.iloc[:,1]
apellidos = df.loc[:,"apellido"]

# accdiendo a la fila
fila_3 = df.loc[2,:]

# accediendo mayor que
mayor_que = df.loc[df["edad"]>26,:]

print(mayor_que)








