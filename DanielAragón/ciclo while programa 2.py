opcion = 0
contactos = []
while opcion != 3:
    print("*****MENÚ*****")
    print("1. Crear nuevo contacto")
    print("2. Ver todos los contactos")
    print("3. Terminar(salir)")
    opcion = int(input("Escoge una opción: "))
    
    if opcion == 1:
        a=input("Nombre: ")
        b=input("Número: ")
        contactos.append(a+"|"+b)
    elif opcion == 2:
        print("\n".join(contactos))
    else:
        print("terminando")
      
