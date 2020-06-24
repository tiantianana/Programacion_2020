# -*- coding: utf-8 -*-
import random 

lista = []

for i in range(21):
    a = random.randint(0,100)
    lista.append(a)

lista_2 = lista 

lista[1] = "Miguel"

"""Cambian el elemento en ambas listas ya que al estar igualadas, todos los 
datos de una se traspasan a la otra"""

lista_3 = []
lista_4 = []

for i in range(21):
    a = random.randint(0,100)
    lista_3.append(a)

for i in range(len(lista_3)):
    b = lista_3[i] 
    lista_4.append(b)

lista_3[1] = "Miguel"

"""En este caso solo varía el valor de la lista_3, puesto a que los datos se 
traspasan de uno en uno a lista_4 andtes de hacer el cambio en un bucle"""