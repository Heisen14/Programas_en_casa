
nombre=input("Ingresa tu nombre")
apellidoPaterno=input("ingresa tu apellido paterno")
apellidoMaterno=input("ingresa tu apellido materno")

nombreCompleto=[nombre,apellidoPaterno,apellidoMaterno]
if " ".join(nombreCompleto) == "Joaquin Aragón Pineda":
    print(nombre+" chinga tu madre, eres un maricón")
else:
    print(" ".join(nombreCompleto))


