# Encontrando el numero mayor de una lista
numeros = [12, 2, 123, 45, 47, 55, 1, 45]
numero_max = max(numeros)
print(f"El numero mas alto es: {numero_max}")

# Encontrando el numero mayor de una lista
numero_min = min(numeros)
print(f"El numero mas alto es: {numero_min}")

# ROUND 
numero = 12.3456789
print(f"numero redondeado: {round(numero, 2)} ")

# BOOL -> si le pasamos 0, false, none o datos vacios nos devuelve False, caso contrario nos devuelve True
resultado = bool()

# ALL -> comprueba si todos los elementos de una lista son verdaderos
resultado = all(["true", 12, 54, "fas"]) #retorna True
resultado = all([None, 12, 54, "fas"]) #retorna False por el none

# SUM -> suma los valores de una lista de numeros
suma_total = sum(numeros)
print(f"la suma total de esos numeros es: {suma_total}")

