# -*- coding: utf-8 -*-

import random
N = int(input("Cual es el tamaño de lista que desea crear? \n"))
lista = []

while N<=0 :
        N = int(input("Tamaño erroneo, porfavor, introduce un tamaño mayor que 0 \n"))
        break

for i in range(N):
    r = random.uniform(1, 49)
    lista.append(r)
    
print(lista)

total = 0

for i in lista:
    total = total + int(i)

print("El total es " ,total)
    


