# -*- coding: utf-8 -*-

caracter = input("Introduzca un caracter por el teclado: \n")

if len(caracter) != 1:
    print("Debe introducir un solo carácter.")
    caracter = input("Introduzca un caracter por el teclado: \n")
    
if caracter >= "0" and caracter <= "9":
   print("Es un número.") 
else:
    print("No es un número.")