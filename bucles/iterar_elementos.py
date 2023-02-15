animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [12, 24, 54, 34, 100]

for animal in animales:
    print(animal)

for numero in numeros:
    resultado = (numero / 2)*100
    print(f"ahora el numero numero es: {resultado}")
    
#  ZIP recorrer dos listas al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(f"recorriendo lista1: {animal}")
    print(f"recorriendo lista2: {numero}")
    
# ENUMERATE forma de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)
    
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice}, y el valor es: {valor}")
    
# ELSE -> usar para aclarar cuando termina el bucle

for numero in numeros: 
    print(f"ejecutando el bucle con numeros: {numero}")
else: print("el bucle termino de trabajar")

# CONTINUE CON IF
for animal in animales: 
    if animal == "cocodrilo":
        continue
    print(f"Tengo de mascota un {animal}")
else: print("termino el bucle pa")

# BREAK .> le pedimos que pare cuando encuentre una coincidencia
for animal in animales: 
    if animal == "loro":
        break 
else: 
    print(f"Tengo de mascota un {animal}")

# FOR EN UNA SOLA LINEA DE CODIGO
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)


