##Un palíndromo es una palabra o frase que se lee igual al derecho y al revés, por ejemplo "anita lava la tina". Tú tarea será crear un programa que reciba una frase como input (esto está automatizado gracias a AutoGradr) y determine si esta frase es un palíndromo.
lista=[]
palindromo=input()
pali=palindromo.lower().split()
contador=0
while contador<len(pali):
    for a in pali[contador]:
        lista.append(a)
    contador+=1
    
pal="".join(lista)
if pal==pal[::-1]:
    print("La frase que ingresaste SÍ es un palíndromo.")
else:
    print("La frase que ingresaste NO es un palíndromo.")