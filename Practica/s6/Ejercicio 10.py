# -*- coding: utf-8 -*-

import random
notas = []

for i in range(5):
    nota = random.randint(1,10)
    notas.append(nota)

minimo = 10
maximo = 0
for i in range(len(notas)):
    if(notas[i] < minimo):
        minimo = notas[i]
    
    if(notas[i] > maximo):
        maximo = notas[i]
t = tuple(notas)       
print("La menor puntuación obtenida es", minimo, "y la mayor puntuación", maximo)

contador = 1
while(contador <= 5):
    if(notas[contador-1] == 1):
        print("Juez", contador, "da al gimnasta 1 punto")       
    else: 
        print("Juez", contador, "da al gimnasta", notas[contador-1],"puntos")
    contador += 1
        