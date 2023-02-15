# Anotamos los datos que tenemos hasta ahora
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dato = 1.5

# Diferencia de duracion

diferencia_con_min = 100 - curso_dato / otros_cursos_min *100
diferencia_con_min = int(diferencia_con_min)

diferencia_con_max = 100 - curso_dato / otros_cursos_max *100
diferencia_con_max = int(diferencia_con_max)

diferencia_con_pro = 100 - curso_dato / otros_cursos_promedio *100
diferencia_con_pro = int(diferencia_con_pro)
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el curso mas rapido,", 
      f"un {diferencia_con_max}% menos que el curso mas lento", 
      f"y un {diferencia_con_pro}% menos que el curso promedio")
print("---------------")
#print(f"el curso de dalto dura un {diferencia_con_max}% menos que el curso mas lento")
#print(f"el curso de dalto dura un {diferencia_con_pro}% menos que el curso promedio")

# Duracion de crudos
crudo_promedio = 5
crudo_dato = 3.5

# Calculamos el tiempo removido en edicion
tiempo_vacio_otros = int(100 - otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_dalto = int(100 - curso_dato / crudo_dato * 100)

print(f"Un curso promedio elimina un {tiempo_vacio_otros}% de contenido en edicion,", 
      f"mientras que Dalto en edicion elimina un {tiempo_vacio_dalto}%")

print("-------------")
# Diferencias con cursos que durante 10 horas
print(f"Ver 10 horas de este curso equivale a ver {int(otros_cursos_promedio / curso_dato * 10)} horas de otros cursos", 
      f"en cambio, ver 10 horas de un curso promedio equivale a ver {int(curso_dato / otros_cursos_promedio * 10)} horas del curso de Dalto")