##Crea un programa que use la lista de números que está adjunta y reciba un número del usuario. Tu programa buscará en la lista la suma que sea igual al número que ingresó el usuario.
lista=[5, 2, 3, 1, 6, 7, 90, 4, 3, 8]
num = int(input())
x={}
list=[]
for x in lista:
    for y in lista:
        if x == y:
            x+y
        elif x+y == num:
            x[x]=y

for x in lista:
    for y in lista:
        if x in x:
            list.append()
