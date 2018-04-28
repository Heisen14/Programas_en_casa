print("Escribe con buena ortografía así como con signos de puntuación")

nombre=input("Ingresa tu nombre")
apellidoPaterno=input("ingresa tu apellido paterno")
apellidoMaterno=input("ingresa tu apellido materno")

nombreCompleto=[nombre,apellidoPaterno,apellidoMaterno]
if " ".join(nombreCompleto) == "Joaquin Aragón Pineda":
    print(nombre+" chinga tu madre, eres un maricón")
elif " ".join(nombreCompleto) == "Daniel Aragón Pineda":
    print(nombre+" eres una chingonería y puedes hacer todo lo que te propongas")
else:
    print(" ".join(nombreCompleto))
