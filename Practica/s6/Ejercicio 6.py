# -*- coding: utf-8 -*-

DNI = int(input("Introduce los 8 dígitos de su DNI: \n"))
letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

value = DNI % 23
print(DNI,letras[value])