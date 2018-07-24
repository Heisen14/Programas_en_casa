print("**********BIENVENIDOS**********")
print("**** Inicio de sesión****")

with open("usuarios.txt") as usuarios:
    usuarios = usuarios.readlines()
    diccionarioA = {}
    diccionarioB = {}
    cartelera = {}
    lista=[]
    lista2=[]
    edades=[]
    print("intento 1 de 3")
    contador=1
    
for usuario in usuarios:
    diccionarioA[contador]=usuario.split('|')[1].strip()
    diccionarioB[contador]=usuario.split('|')[0]
    contador+=1

usu=diccionarioB.values()
contra=diccionarioA.values()


contador = 0
for u2 in usu:
    lista.append(u2)
    contador += 1
contador = 0
for c2 in contra:
    lista2.append(c2)
    contador += 1

intentos = 1
while intentos <=3:
    u=input("Usuario: ")
    c=input("Contraseña: ")
    if u in lista:
        valor=lista.index(u)
        if c == lista2[valor]:
            with open("peliculas.txt") as peliculas:
                peliculas = peliculas.readlines()
                peli=0
                intentos=4
        else:
            intentos += 1
            if intentos == 4:
                exit()
            else:
                print("Contraseña equivocada")
                print ("intento", intentos,"de 3")
    else:
        intentos += 1
        if intentos == 4:
            exit()
        else:
            print("Usuario inexistente: ")
            print ("intento", intentos,"de 3")
            
cine=1
while cine!=0:  
    for pelicula in peliculas:
        cartelera[peli] = pelicula
        print(peli,'.',pelicula)
        peli+=1
    cine=int(input("¿Qué pelicula quieres ver? (0 para salir)"))
    if cine == 0:
        exit()
    else:
        boletos=int(input("¿Cuantos boletos quiere comprar?"))
        contador = 0
    while boletos > contador:
        edades.append((int(input("Ingresa las edades: "))))
        if edades[contador]<13:
            edades[contador]=50
            print(edades[contador])
            contador+=1
        else:
            edades[contador]=100
            print(edades[contador])
            contador+=1
            
    total=0
    for i in edades:
       total=total+i
    print("El total es de $", total ," para la pelicula", cine)
    edades=[]
                
           
        
exit()

        


           
    
