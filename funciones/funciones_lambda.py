# creando una funcion lambda
# es una funcion anonima 
# y es mucho mas corta que hacer una funcion normal
# se la asignamos a un valor y no es necesario ni un return 
multiplicador_dos = lambda x : x*2
print(multiplicador_dos(10))

# creando una funcion comun para ver si los numeros que numeros son par
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def es_par(num):
    if (num%2 == 0): #si el resto es igual a 0 al dividirlo por 2 es porque es par
        return True
# usando filter para esto
numeros_pares = filter(es_par, numeros)

# ahora vamos a crear lo mismo pero con lambda
numeros_pares = filter(lambda x : x%2 == 0,numeros)
print(list(numeros_pares))
