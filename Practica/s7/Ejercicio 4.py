# -*- coding: utf-8 -*-

def factorial(x):
    if(x == 0): return 1
    
    if(x == 1): return 1
    
    if(x > 1):
        i = 1
        valor = 1
        while(i <= x):
            valor *= i
            i += 1
        return valor

print(factorial(64))