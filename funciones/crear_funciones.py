# creando nuestras propias funciones
#ES IMPORTANTE VER QUE SIEMPRE SE EMPIEZA CON DEF()
#def saludar():
 #   print("Hola pa, todo tranqui vos?")
    
#saludar()

# Los parametros son variables que se crean para ser utilizadas dentro de una funcion y despues no se usan mas
# CREANDO UNA FUNCION QUE TENGA PARAMETROS
#nombre_in = input("Cual es tu nombre? ")
#sexo_in = input("cual es tu sexo? ")
def saludar(nombre, sexo): 
    sexo = sexo.lower()
    if (sexo == "mujer"): 
        adjetivo = "reina"
    elif (sexo == "hombre"): 
        adjetivo = "titan"
    else: adjetivo = "amor"
    
    print(f"Hola {nombre}, mi {adjetivo}, como estas?")
    
saludar("LUCAS", "HOMBRE")

# CREANDO UNA FUNCION PARA GENERAR CONTRASEÑAS

def crear_contraseña(num): 
    charts = "abcdefghij"
    num_entero = str(num) #lo convertimos a string
    num = int(num_entero[0]) #lo convertimos en int al numero
    c1 = num - 2 #estos sirven para a la hora de generar la contraseña, generar posiciones aleatorias dentro de la cadena
    c2 = num 
    c3 = num - 5
    contraseña = f"{charts[c1]}{charts[c2]}{charts[c3]}{num**3}" #Es como si le dijieramos charts[1], con la diferencia que ese "1", esta determinado por los calculos aleatorios de arriba
    return contraseña #la mayoria de las funciones tiene un return, es decir tiene el valor pero no te lo tira a consola de una, sino que vos lo tenes que visualizar con print

contra = crear_contraseña(456)
print(contra)

# CREANDO UNA FUNCION PARA SUMAR VALORES
# El "*" hace referencia al parametro args
def suma(*numeros):
    num_suma = sum(numeros)
    return num_suma

resultado = suma(2,4,78,24,2,10)
print(resultado)