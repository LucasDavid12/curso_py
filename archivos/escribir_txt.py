# Con el "w", le estoy diciendo que tengo un permiso de escritura
# si "w" no encuentra el archivo, crea uno nuevo
# si queremos agregar una linea, en vez de poner "w", hay que poner "a"
with open("curso_python\\archivos\\texto_lucas.txt", "w") as archivo:
    #archivo.write("reescribir el archivo (elimina lo anterior pa)")
    # creamos varias lineas de texto pero hay que pasarlas como una lista, entre []
    #archivo.writelines(["hola pa como estas? ", "Todo tranquilo y vos? "])
    # para escribir varias lineas pero con un salto hay que usar \n
    archivo.writelines(["Hola pa como estas? \n", "Todo tranqui vos?\n"])
    # si agrego uno nuevo writelines debajo, lo voy agregar a al archivo
    archivo.writelines(["Hola mamu como estas? \n", "Todo mal"])
    
with open("curso_python\\archivos\\texto_lucas.txt", "a") as archivo:
    archivo.write("\nAhora estoy agregando una linea sin eliminar lo anterior")    