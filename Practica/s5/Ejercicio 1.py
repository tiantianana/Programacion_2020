# -*- coding: utf-8 -*-

dinero = 10
pin = 1234

print ("Introduzca el pin")
x = int(input())

if x != pin :
    for i in range(2):
        x = int(input("Introduce el pin \n"))
        if i == 1 and x != pin:
            print ("Se ha agotado el número de intentos")
        elif x == pin:
            print ("pin correcto")
            dinero = int(input("Cuanto dinero quiere sacar"))
            break
else:
    print ("pin correcto")
    dinero = int(input("Cuanto dinero quiere sacar"))