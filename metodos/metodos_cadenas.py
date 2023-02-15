# Trabajar con cadenas de texto
cadena1 = "Hola soy Lucas"
cadena2 = "Bienvenido a la universidad"

#FUNCION -> dir(cadena1) o len(candena1)
#METODO -> cadena1.upper() o cadena1.count()
# dir() nos da las especificaciones de lo que podemos hacer con ese tipo de dato. Por ej si es un string te va a mostrar como pasarla a mayuscula pero si es un float te va mostrar como poder redondearlo -> ES UNA FUNCION, NO UN METODO
#resultado = dir(cadena1) 

# UPPER -> convierte todo en mayuscula
resultado = cadena1.upper() #tener en cuenta que los metodos funcionan seguido de, es decir primero se le asigna la variable con la que se va a trabajar punto y el metodo 

# LOWER <- convierte en miniscula
resultado1 = cadena1.lower()

# CAPITALIZE <- primera letra en mayuscula
resultado2 = cadena1.capitalize()

# FIND <- buscamos una palabra o caracter (cadena) en la cadena de texto
resultado3 = cadena1.find("w") # si no encuentra lo que esta pidiendo te va a tirar -1

# INDEX <- igual que FIND con la diferencia que cuando no encuentra nada, te tira error
resultado4 = cadena1.index("H")

# ISNUMERIC <- si es numerico devulve True y sino devuelve False
resultado5 = cadena1.isnumeric()

# ISALPHA <- si es alfanumerico devuelve True y sino devuelve False -> alfanumerico solo reconoce las letras de a - z sin espacios , solo de esa forma va a tirar true
resultado6 = cadena1.isalpha()

# COUNT <- cuenta la cantidad de veces que se repeite una cadena 
resultado7 = cadena1.count("a")

# LEN <- cuenta los caracteres OJO ES UNA FUNCION
resultado8 = len(cadena1) #FUNCION

# STARTSWITH <- verificamos si una cadena compienza con lo que nosotros buscamos, si es asi nos devuelve True
resultado9 = cadena1.startswith("H")

# ENDSWITH <- Verificamos si una cadena termina con lo que nosotros buscamos, si es asi nos devuelve True
resultado10 = cadena1.endswith("Lucas")

# REPLACE <- remplaza una cadena de texto con una nueva
resultado11 = cadena1.replace("Hola", "Holis") # si no encuentra coincidencia se queda con la misma cadena

# SPLIT <- separa la cadena es una lista segun el parametro dado (es igual a unnest() es R)
resultado12 = cadena1.split(" ")
resultado13 = resultado12[1].upper()
print(resultado8)







