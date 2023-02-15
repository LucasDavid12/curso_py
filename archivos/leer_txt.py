# Si en algun momento aparece algun caracter especial, al lado de la url hay que poner encoding="UTF-8"
archivo = open("curso_python\\archivos\\texto_lucas.txt")
#print(archivo.read())
# leer por lineas, nos devuelve una lista con las lineas del texto
#lineas = archivo.readlines()
#
lineas_1 = archivo.readline()
# una vez que terminamos de trabajar con el archivo hay que cerrarlo con close
archivo.close()
# una vez que se cerro abria que usar de vuelta la funcion open
# forma optima de abrir un archivo, se abre, se arma el codigo segun la necesidad y se cierra
with open("curso_python\\archivos\\texto_lucas.txt") as archivo:
    print(archivo.read())