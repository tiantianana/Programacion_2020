# -*- coding: utf-8 -*-

f1 = 12345678901234567.123456789001234568
f2 = 123456789001234568.12345678901234567

f = f1*f2
print(f)

# El resultado es un numero exponencial 1.5241578751867094e+33

f1 = 12345678901234567.0
f2 = 123456789001234568.0

f = f1**f2
print(f)

# Se produce un overflow error, resultado fuera de rango