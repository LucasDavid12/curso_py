# trabajar con listas

# LIST -> crea una lista ES UNA FUNCION
lista = list(["Hola", "lucas", "como"])
lista2 = list(["mama", "papa", True, 22])
lista3 = list([23, 43, 1, 235, 22, 4, 7, 45, 1234, 678])
#print(lista)

# LEND -> te devuelve la cantidad de elementos de la lista
resultado = len(lista) #FUNCION 

# APPEND -> agrega elemento a la lista directamente, no hace falta hace print a resultado2 en este caso sino que ya directamente se la agrega a la variable lista
resultado2 = lista.append("estas")

# INSERT -> se agrega un elemento a la lista pero aclarando la posicion
resultado3 = lista.insert(2, "Lic")

#EXTEND -> agrega una lista a otra lista
resultado4 = lista.extend(lista2)

# POP -> eliminar un elemento de la lista con su indice
resultado5 = lista.pop(-1) #con el - se eliminar el ultimo elemento de la lista

# REMUVE -> elimina con elemento de la lista por su nombre
resultado6 = lista.remove("Lic")

# CLEAR -> elimina a todos los elementos de la lista
#resultado7 = lista.clear()

# SORT -> Ordena de menor a mayor los elementos de una lista (aunque solo los int o float) no puede hacerlo con string
lista3.sort(reverse=True) #sort() de menor a mayor, con reverse de mayor a menor

# REVERSE -> invierte el orden de la lista NO LA ORDENA COMO SORT, el orden de como esta directamente lo da vuelta
lista3.reverse()

# INDEX -> En las lista index busca el elemento completo, en los medetodos de cadenas si yo buscaba una letra con index y estaba me iba a tirar la posicion, aca no, solo nos va a dar un resultado cuando coincida el elemento entero
resultado7 = lista3.index(1234)

print(resultado7)




