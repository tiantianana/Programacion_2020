# -*- coding: utf-8 -*-

operadores = ["+", "-", "*", "/", "//", "**"]

num1 = float(input("Introduzca el primer número: \n"))
num2 = float(input("Introduzca el segundo número: \n"))
operador = input("Introduzca el operador: \n")

esOperador = False

while esOperador == False:
    for i in operadores:
        if operador == operadores[0]:
            suma = num1 + num2
            print(suma)
            esOperador = True
            break
        
        if operador == operadores[1]:
            resta = num1 - num2
            print(resta)
            esOperador = True
            break
        
        if operador == operadores[2]:
            multiplicacion = num1 * num2
            print(multiplicacion)
            esOperador = True
            break
    
        if operador == operadores[3]:
            division = num1 / num2
            print(division)
            esOperador = True
            break
    
        if operador == operadores[4]:
            division_entera = num1 / num2
            print(division_entera)
            esOperador = True
            break
        
        if operador == operadores[5]:
            exponente = num1 ** num2
            print(exponente)
            esOperador = True
            break
        
        else:
            print("Operador incorrecto")
            esOperador = True 
            break
    