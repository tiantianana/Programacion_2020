# -*- coding: utf-8 -*-

num = (input("Introduzca un número por teclado: \n"))
cuadrado = 0
try:
    numero = float(num)
except ValueError:
    numero = None

if numero == None:
    print("Incorrecto. Introduzca un número por teclado \n")
elif numero == int(numero):
    cuadrado = numero ** 2
    print(cuadrado)
else:
     cuadrado = numero ** 2
     print(cuadrado)

