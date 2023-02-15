# Operadores de pertenecia (in / not in)
nombre = "lucas"
bienvenida = f"Hola {nombre} como estas?" #En este caso si se agrega un tipo de dato que no es un caracter a la variable nombre, la f por delante y los corchetes lo van a transformar a caracter
del bienvenida # elimina la definicion de bienvenida

print("ola" in bienvenida) # le estoy diciendo que me busque en la variable bienvenida los caracteres "ola" -> TRUE
print("pedro" not in bienvenida) # le diciendo que busque si no esta pedro en bienvenida -> TRUE 

#Datos compuesto
lista = ["Lucas", "Vidal", True, 1.75] #se define la variable lista con varios elementos adentro
lista[0] # me va a mostrar el primer elemento de la lista

tupla = ("Lucas", "Vidal", True, 1.75) #una tupla es un elemento que no se puede modificar, si mas adelante quiero modificar algo de la lista no lo voy a poder hacer
tupla[1] # se llama el elemento con corchetes aunque se haga con parentesis

# Creando un conjunto (set) -> no admite duplicados, buena forma de eliminarlos

conjunto = {"Lucas", "Vidal", True, 1.75} #no se puede llamar a los elementos por el indice

# Crando un diccionario (dict)
diccionario = {
    "nombre" : "Lucas", #clave : valor
    "apellido" : "Vidal",
    "emocionado" : True,
    "altura" : 1.75
}
print(diccionario["altura"])