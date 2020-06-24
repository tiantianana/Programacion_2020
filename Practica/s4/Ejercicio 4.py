# -*- coding: utf-8 -*-

entero1 = int(input("Inserte el primer número entero: \n"))
entero2 = int(input("Inserte el segundo número entero: \n"))

if entero2 == 0:
    print("No se puede dividir por cero usando enteros")
else:
    div = entero1/entero2
    print("El resultado de la división es:")
    print(div)