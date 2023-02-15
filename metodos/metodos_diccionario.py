# trabajar con diccionarios
diccionario = {
    "nombre" : "lucas",
    "apellido" : "vidal", 
    "carrera" : "cs politica", 
    "desempeño" : "recibido", 
    "promedio" : 7.89
}

# KEYS -> nos muestra las claves, es decir los elementos a la izquierda 
resultado = diccionario.keys()

# GET -> le pasamos la clave y nos devuelve el resultado de esa clave especifica
resultado2 = diccionario.get("carrera") #si no encuentra coincidencia tira none pero no para el programa

# CLEAR -> elimina todo del diccionario

#POP -> elimina un elemento del diccionario
resultado3 = diccionario.pop("nombre")

print(diccionario)
