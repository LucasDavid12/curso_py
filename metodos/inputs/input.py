# pedirle un dato al usuario
nombre = input("dame tu nombre: ") # lo que nos va a dar input es un texto, si o si
edad = input("tu edad es: ")
carrera = input("que carrera estudias? ")
promedio = input("por ultimo, cual es tu promedio en la univerdad) ")
#concateno el input 
print(f"Mi nombre es {nombre},", 
      f"tengo {edad} años", 
      f"estudio {carrera}, en la UCALP", 
      f"y mi promedio es de {promedio}")
# si ponemos una input para que ponga un numero, en la salida lo tenemos que converir a int o a float
#edad = input("Cuantos años tenes?: ")
#edad = int(edad)
#print(f"tengo {edad} años")
#print(int(16.9))