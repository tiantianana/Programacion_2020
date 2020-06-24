# -*- coding: utf-8 -*-
import random

lista = []

for i in range(20):
    a = random.randint(1,9)
    lista.append(a)

num = int(input("Escribe el número que desea buscar: \n"))

posiciones = []

for i in range(len(lista)):
    if(lista[i] == num):
        posiciones.append(i)
        
if(len(posiciones) > 0):
    print("El número que busca está en la lista en las posiciones: ")
    print(posiciones)
else: print("El número no está en la lista")