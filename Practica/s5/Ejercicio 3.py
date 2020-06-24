# -*- coding: utf-8 -*-
import random
r = random.randrange(1, 20)

print("Averigue el número que estoy pensando")
z = int(input())
i = 0
while z != r :
    if ( z < r ): 
        print("El numero que estoy pensando es mayor que" ,z)
    else :
        print("El numero que estoy pensando es menor que" ,z)
    z = int(input("Pruebe otra vez \n"))
    i += 1

print ("Ha acertado el número en :" ,i, "intentos")

