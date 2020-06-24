# -*- coding: utf-8 -*-

print("¿Cómo se llama?")
nombre1 = input()

print("¿Cúal es su edad?")
edad1 = input()

print("¿Cómo se llama?")
nombre2 = input()

print("¿Cúal es su edad?")
edad2 = input()

if edad1 > edad2:
    print(nombre1+ " es mayor que " +nombre2)
    
elif edad1 < edad2:
    print(nombre1+ "es menor que" +nombre2)
    
else:
    print(nombre1+ " y " +nombre2+ " tiene la misma edad")