import csv 

# Para leer los csv usamos csv.reader
with open("curso_python\\archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)