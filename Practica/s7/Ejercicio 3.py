# -*- coding: utf-8 -*-
lista = [1, 2, 2, 3, 3, 4, 4, 5, 7]

def count(list, x):
    contador = 0
    for i in lista:
        if x == i:
            contador += 1
    return contador


def index(list, x):
    resultado = -1
    posicion = 0
    for i in list:
        if x == i:
            resultado = posicion
        posicion += 1

    print(resultado, "resultado")
    return resultado


#def append(list, x):
    

def find(list, x):
    encontrado = False
    contador = 0
    for i in lista:
        if x == i:
            encontrado = True
            contador += 1
    return encontrado

def remove(x):
    contador = 0
    for i in lista:
        if x == i:
            del(lista[contador])  
        else:
            contador += 1
    print(lista, "remove el 4")
        

def removeAll(list):
    print(lista, "lista1")
    for i in range(len(lista)):
        del(lista[0])    
    print(lista, "lista")
    return lista
        


a = count(lista, 4)
b = index(lista, 3)
#c = append(lista, 9)
d = find(lista, 2)
#e = insert(lista, 9, 4)
f = remove(7)
g = removeAll(lista)