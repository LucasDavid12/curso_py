diccionario = {
    "nombre" : "lucas",
    "apellido" : "vidal", 
    "carrera" : "cs politica", 
    "promedio" : 7.85
}

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
else: print("se termino el bucle pa")