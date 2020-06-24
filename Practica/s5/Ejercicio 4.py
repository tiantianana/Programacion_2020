# -*- coding: utf-8 -*-

num_1 = int(input("Introduzca el primer número: \n"))
num_2 = int(input("Introduzca el segundo número: \n"))

i = 1
multiplicacion = 0

while i <= num_2:
    multiplicacion += num_1
    i += 1 
    
print(multiplicacion)