print("**********BIENVENIDOS**********")
print("**** Inicio de sesión****")

with open("usuarios.txt") as usuarios:
    usuarios = usuarios.readlines()
    diccionarioA = {}
    diccionarioB = {}
    diccionarioC = {}
    intentos = 0
    print("intento ", intentos,"de 3")
    usu=1
    u=input("Usuario: ")
    while intentos <=3:
        for usuario in usuarios:
            diccionarioC[usu] = usuario.split('|')[0]
            if u==diccionarioC[usu]:
                c=input("Contraseña: ")
                if usuario.split('|')[1]==c:
                    with open("peliculas.txt") as peliculas:
                        peliculas = peliculas.readlines()
                        peli=1
                    for pelicula in peliculas:
                        print(peli,'.',pelicula)
                        peli+=1
                else:
                    print("Contraseña incorrecta")
                    intentos+=1
                    print("intento ", intentos,"de 3")
                    c=input("Contraseña: ")
            elif u=="salir":
                exit()
            else:
                usu+=1
        
    print("Usuario inexistente")
    intentos+=1
    print("intento ", intentos,"de 3")
    
    exit()
    
