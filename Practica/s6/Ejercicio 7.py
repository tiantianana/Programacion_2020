# -*- coding: utf-8 -*-

tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

N = int(input("Introduzca un número \n"))

    
if N == 0:
    print("error")
    
while N!= 0:
    if N>1 and N<len(tupla):
        print(tupla[N+1])
        break
    else :
        print("Error, porfavor introduzca otro número")
        N = int(input("Introduzca un número \n"))
    

    