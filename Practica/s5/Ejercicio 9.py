# -*- coding: utf-8 -*-

a = int(input("Introduce el numero tope de generación de numeros perfectos \n"))
b = a
sumatoria = 0
for i in range(1, b) :
    if b%i == 0 :
        a -= i
        print(i, "i")
        print(a, "a")
if a == 0 :
    print("El numero es perfecto")
else:
    print("El numero no es perfecto")

