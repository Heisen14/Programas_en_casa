num=int(input())
lista=[]

range(1,num+1)
for x in range(1,num+1):
    if num%x == 0:
        lista.append(x)

print(lista)