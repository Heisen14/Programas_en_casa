import random
print("****BIENVENIDO AL ADIVINADOR****")

limite = int(input("Dame un limite superior: "))
print("Jugando números entre 1 y ",limite)

x = random.randint(1,limite)
rango = "dame un numero entre 1 y ",limite
numeroDicho=int(input(rango))

contador=1
while numeroDicho != x:
    contador += 1
    numeroDicho=int(input(rango))
    
print("Adivinaste en ",contador, "intentos")