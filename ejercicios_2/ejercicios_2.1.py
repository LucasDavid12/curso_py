# datos del ejercicio
# pedir el nombre y la edad de los chicos que fueron a la clase
# el de edad mas alta va a ser el profesor y el de mas baja el asistente 
def obtener_compañeros(cantidad_compañeros): 
    compañeros = []
    for i in range(cantidad_compañeros):
        # le pedimos que ingrese el nombre y la edad
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        # agregamos info a la lista -> compañero
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0] # el argumento de la derecha es la posicion en la lista de la variable (nombre) y el de la izquierda la posicion dentro de la variable nombre (cuando es 0 es el primero y como esta ordenado de menor a mayor implica que sea mas chico)
    profesor = compañeros[-1][0]
    return asistente,profesor

# desempaquetamos lo que nos arroja la funcion
asistente,profesor = obtener_compañeros(5)
print(f"El profesor es {profesor}, y su asistente es {asistente}")