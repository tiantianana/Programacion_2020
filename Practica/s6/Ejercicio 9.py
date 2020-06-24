# -*- coding: utf-8 -*-

b = input("Introduzca una frase \n")
a = b.upper()
print(b)
matriz = []
matriz[:0] = a
print(matriz)

print(matriz)

unico = []
for x in matriz:
    if x not in unico:
        unico.append(x)
        
print(unico)
unico.remove(" ")

unico = tuple(unico)
print(unico)

