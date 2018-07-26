##Dado un año, imprime el siglo en el que se encuentra. El primer siglo va desde el año 1 hasta e incluyendo el año 100, el segundo - desde el año 101 hacia arriba e incluyendo el año 200, etc.
año=int(input())
siglo=año/100
round(siglo,-1)

if año%100==0:
    print(int(siglo))
else:
    print(int(siglo+1))
    
