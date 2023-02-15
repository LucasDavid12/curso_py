# cadena de texto, con comillas simples en la misma linea

"string"

'string'

#cadena de texto, con comillas triples se puede poner enter y seguir abajo

"""presetancion:
                 nombre: lucas
                 apellido: vidal"""

# numero entero (int)

40

#numero frotante (froat)

40.5

# boleano: dos posibilidades (primera letra en mayuscula)

True

False

# variables 

numero = 10

# el valor que ya tiene mas (en este caso) lo que esta despues del igual
# tener en cuenta que esto sirve para redefinir la variable todo el tiempo

numero +=1 

# la variable pasa a ser 11 y lo si escribo otra linea abajo (igual) numero pasaria a ser 12
# CONCATENAR -> union de cadenas de texto

nombre = "Lucas"
bienvenida = "Hola " + nombre + " como estas?" #Esta es la forma mas simple pero que puede llegar a generar un error si la variable que se aloja como nombre no es un texto, por eso

# segunda forma de concatenar = fstring

nombre = "lucas"
bienvenida = f"Hola {nombre} como estas?" #En este caso si se agrega un tipo de dato que no es un caracter a la variable nombre, la f por delante y los corchetes lo van a transformar a caracter
del bienvenida # elimina la definicion de bienvenida