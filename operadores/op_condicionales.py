# OPERADORES CONDICIONALES
#if True:
    # la condicion se ejecuta
   
#if False: 
    # accion no se ejecuta
# else: lo que pasa si no se cumple
# si la condicion se cumple (True) se va ejecutar lo que este dentro de if
# si la condicion no se cumple (False) se va a ejecutar lo que este dentro de else
    
edad = 19
if edad >= 18: 
    print("podes pasar")
else : 
    print("no podes pasar")

# else + if = un camino intermedio cuando no cumple una primer condicion pero puede llegar a cumplir una segunda

ingreso = 100000
if ingreso > 10000: 
    print("estas bien en cualquier parte del mundo")
elif ingreso > 1000: 
    print("estas bien en latinoamerica")
else:                         # atencion que else del final no cumple ninguna condicion ya que lo que recibe es la orden del elif, si su condicion no se cumple pasa a la de else
    print("sos pobre")
 
# Convinar todo lo anterior de diferentes maneras 
ingreso_mensual = 7000
gasto_mensual = 2000

if ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual > 1000:  #si el ingreso al mes menos los gatos son mayor a mil, estas bien pero si no es asi "estas gastando mucho"
        print("ahora si estas bien")
    else:
        print("estas gastando banda")
elif ingreso_mensual > 1000:
    print("Estas bien para latinoamerica")
