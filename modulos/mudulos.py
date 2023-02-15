# los modulos son todos los archivos que tiene extension .py
# Nos sirve para llamar funciones o trabajos que realizamos en otro archivo
# usamos la funcion saludar del modulo "modulo_saludar.py"

#import modulo_saludar #el modulo aparte se comporta como un metodo

#saludo = modulo_saludar.saludar("lucas")
#print(saludo)

# para asignarle un nuevo nombre al modulo (ex funcion llamada con import) podemos usar as

# import modulo_saludar as m_saludar -> ahora cuando llamemos al modulo va a ser m_saludar y no modulo_saludar

# IMPORTAR COMO FUNCION -> a traves from
from modulo_saludar import saludar
saludo = saludar("lucas")
print(saludo)

# SI EL MODULO ESTA UNA CARPETA DENTRO DE LA MISMA CARPETA ES:
#from nombre_de_carpeta.modulo import funcion

# SI EL MODULO ESTA FUERA DE LA CARPETA ES:

#import sys
#print(sys.path)
# CAMBIAR LA RUTA DEL MODULO -> sys.path.append("C:\\Users\\Usuario\\Desktop\\Python\\curso_python\\modulos")
