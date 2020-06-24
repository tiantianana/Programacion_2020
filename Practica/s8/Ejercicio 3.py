# -*- coding: utf-8 -*-
import random

class Dado:
    nombre = " "
    tiradas = 0
    
    def __init__(self, nombre, n):
        self.name = nombre
        self.tiradas = n
    
    def Lanzamientos(self):
        lanzamientos = []
        for i in range(self.tiradas):
            num = random.randint(1,6)
            lanzamientos.append(num)
        return lanzamientos 
              
    def Maximo(self):
        num_dados_iguales = []
        i = 1
        while i <= 6:
            num_dados_iguales.append((self.Lanzamientos()).count(i))
            i += 1
        tuple(num_dados_iguales)
        maximo = max(num_dados_iguales)
        return maximo
            
    def Empate(self):
        suma = 0
        for i in range(len(self.Lanzamientos())):
            suma += self.Lanzamientos()[i]
        return suma
    
nombre = input("Deme el nombre del jugador 1: \n")
nombre_2 = input("Deme el nombre del jugador 2: \n")
num = int(input("¿Cuántas veces se ha jugado? \n"))
jug_1 = Dado(nombre, num)
jug_2 = Dado(nombre_2, num)
def Jugada(play1, play2):
    resultado = ""
    if(play1.Maximo() > play2.Maximo()):
        resultado = "El ganador es " + nombre
    elif(play1.Maximo() < play2.Maximo()):
        resultado = "El ganador es " + nombre_2
    elif(play1.Maximo() == play2.Maximo()):
        print("Hay un empate. El desempate se determinará con la suma de los dados")
        if (play1.Empate() >= play2.Empate()): resultado = "El ganador es " + nombre
        else: resultado = "El ganador es " + nombre_2
    return resultado

print(Jugada(jug_1, jug_2))