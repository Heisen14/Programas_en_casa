# Prueba 1
promedio=float(input("Ingresa tu promedio (con puntos decimales):"))
origen=input("Ingresa el estado donde naciste:")
miembro=input("¿Es miembro de inviertete?: (s/n)")
#Prueba 2
velocidadDeComida=int(input("¿Cuántos tacos te comes en 45 minutos?:"))
libros=int(input("¿Cuántos libros lees al año?"))
#Resultados de pruebas
pruebaUno= (promedio<=9.0 and origen=="Oaxaca" and miembro=="s")
pruebaDos= (velocidadDeComida==10 and libros==12)
if pruebaUno== True and pruebaDos==True:
    print("Eres ganador de la beca Alan Turing")
elif pruebaUno== True:
    print("No pasaste la segunda prueba :c")
else:
    print("No pasaste la prueba uno")
