nombres = ["Lucas", "Enrique", "Candela", "Micaela", "Joaquin"]
apellidos = ["Vidal","Marzo", "Gimenez", "Godoy", "Pastormerlo"]

# registrar esta info en un txt
with open("nombres_y_apellidos", "w") as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres, apellidos)]
    