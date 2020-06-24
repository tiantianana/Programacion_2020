# -*- coding: utf-8 -*-

totalSegundos = int(input("Introduce el número de segundos a convertir: \n"))

if totalSegundos >= 3600:
    horas = int(totalSegundos / 3600)
    totalSegundos -= (horas * 3600)
    minutos = int(totalSegundos / 60)
    totalSegundos -= (minutos * 60)
    segundos = totalSegundos
    
elif totalSegundos >= 60:
    horas = 0
    minutos = int(totalSegundos / 60)
    totalSegundos -= (minutos * 60)
    segundos = totalSegundos
    
else:
    horas = 0
    minutos = 0
    segundos = totalSegundos
    
print(horas,":",minutos,":",segundos)
    