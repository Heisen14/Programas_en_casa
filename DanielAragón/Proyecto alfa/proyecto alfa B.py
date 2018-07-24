print("**********BIENVENIDOS**********")
print("**** Inicio de sesión****")

with open("usuarios.txt") as usuarios:
    usuarios = usuarios.readlines()
    diccionarioA = {}
    diccionarioB = {}
##    diccionarioC = {}
    intentos = 1
##    print("intento ", intentos,"de 3")
##    usu=1
    u=input("Usuario: ")
    c=input("Contraseña: ")
    contador=1
for usuario in usuarios:
    diccionarioA[contador]=usuario.split('|')[1]
    diccionarioB[contador]=usuario.split('|')[0]
    contador+=1
if  c==diccionarioA[3]:
    print("Hola")
##           with open("peliculas.txt") as peliculas:
##                        peliculas = peliculas.readlines()
##                        peli=1
##            for pelicula in peliculas:
##                print(peli,'.',pelicula)
##                peli+=1
else:
    contador+=1
            