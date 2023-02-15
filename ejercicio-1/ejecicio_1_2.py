# Ejercicio 1 - Punto 2
# Para contar palabras tener en cuenta que split sirve para separarlas y ahi si las podemos contar con len
# Si contamos directamente con len nos va a contar la cantidad de caracteres (contando los espacios)
frase = input("Decime algo y te calculo cuanto tiempo tardarias en decirlo: ")
cantidad_palabras = len(frase.split(" "))
# En promedio las personas hablan dos palabras por segundo
if cantidad_palabras > 120:
    print("Para loco, eso es un monton")
if cantidad_palabras < 10:
    print("Che loquito esas son re pocas palabras")
print(f"Dijiste en total {cantidad_palabras} palabras. Esa frase tardarias diciendola {cantidad_palabras / 2} segundos")
print(f"Dalto tardaria diciendola {(cantidad_palabras/2)*0.3} segundos, ya que habla un 30% mas rapido")
