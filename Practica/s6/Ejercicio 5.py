# -*- coding: utf-8 -*-
import random
intentos = 1
lista = []

for i in range(100):
    r = random.randint(1, 100)
    print("Es el numero" ,r)
    respuesta = input()
    
    if r in lista:
        print("Ese número esta repetido")
        continue
    else :
        lista.append(r)
    
    if respuesta == "True":
        print("Ha acertado")
        print("El numero de intentos fueron" ,intentos)
        break
    else : 
        print("No ha acertado")
        print("Lleva " ,intentos)
        intentos +=1
        continue

    if intentos == 100:
        print("Estas mentendo, he intentado todos los números")
        
        
print(lista)