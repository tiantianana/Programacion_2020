# -*- coding: utf-8 -*-

sueldo = int(input("Introduzca su sueldo: \n"))

antiguedad = int(input("Introduzca su antigüedad: \n"))

if sueldo < 500:
    if antiguedad > 10:
        sueldo = sueldo * 1.05
        print("Sueldo a pagar:",sueldo)
      
    if antiguedad <= 10:
        sueldo = sueldo * 1.1
        print("Sueldo a pagar:",sueldo)
else:
    print("Sueldo a pagar:",sueldo)
