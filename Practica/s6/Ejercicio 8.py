# -*- coding: utf-8 -*-

frase = input("Introduze usa frase que quiera \n")
matriz = []

for i in range(len(frase)):
    if(frase[i] != " "):
        matriz.append(frase[i])

tupla_frase = tuple(matriz)
print(tupla_frase)