# -*- coding: utf-8 -*-

edad = int(input("Introduzca su edad: \n"))
precio = 9

if edad < 26:
    if edad < 5:
        precio -= precio * 0.6        
    precio -= precio * 0.2
elif edad > 65:
    precio -= precio * 0.4

print("El precio de la entrada es de: ")
print(precio, "euros")