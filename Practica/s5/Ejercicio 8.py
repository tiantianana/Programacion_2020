# -*- coding: utf-8 -*-
menores = range(1,5)
mayores = range(6,11)
respuesta_1 = input("El número ¿es mayor o menor de 5? (mayor/menor) \n")

if respuesta_1 == "mayor":
    for i in mayores:
        print(i)
       
if respuesta_1 == "menor":
    for i in menores:
        print(i)
          
respuesta_2 = input("¿Es par o impar? (par/impar) \n")

while(respuesta_2 == "par"):
    if(respuesta_1 == "mayor"):
        for i in mayores:
            if (i % 2 == 0):
                print(i)
        break   
    else:
       for i in menores: 
           if(i % 2 == 0): 
               print(i)
       break

while(respuesta_2 == "impar"):
    if(respuesta_1 == "mayor"):
        for i in mayores:
            if (i % 2 != 0):
                print(i)
        break
    else:
       for i in menores: 
           if(i % 2 != 0): 
               print(i)
       break

respuesta_3 = input("¿Extremo superior o inferior? (superior/inferior) \n")

if(respuesta_3 == "superior"):
    if(respuesta_1 == "mayor" and respuesta_2 == "par"):
        print(10)
    elif(respuesta_1 == "mayor" and respuesta_2 == "impar"):
        print(9)
    elif(respuesta_1 == "menor" and respuesta_2 == "par"):
        print(4)
    else: print(3)
    
if(respuesta_3 == "inferior"):
    if(respuesta_1 == "mayor" and respuesta_2 == "par"):
        print(6)
    elif(respuesta_1 == "mayor" and respuesta_2 == "impar"):
        print(7)
    elif(respuesta_1 == "menor" and respuesta_2 == "par"):
        print(2)
    else: print(1)