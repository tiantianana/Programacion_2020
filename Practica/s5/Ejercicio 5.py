# -*- coding: utf-8 -*-

num = int(input("Inserte un número: \n"))
suma = 0
i = 1

while 0 < i <= num:
    if(i % 2 == 0):
        suma += 1
    i += 1
    
print(suma)