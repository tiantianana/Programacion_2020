# -*- coding: utf-8 -*-

a = 3
b = 8
c = 3.0
r = a == 0
s = a != 0
t = a <= b
u = b >= a
v = b > a
w = b < a
x = c == 3.0

print("r:", r) 
# El resultado es false ya que a no es igual a 0 (3 != 0)

print("s:", s)
# EL resultado es true ya que a si es distinto de 0, (3 != 0)

print("t:", t)
# El resultado es true ya que a es menor o igual que b (3 <= 8) 

print("u:", u)
# El resultado es true ya que b es mayor o igual que a (8 >= 3)

print("v:", v)
# El resultado es true ya que b es estrictamente mayor que a (8 > 3)

print("w:", w)
# El resultado es false ya que b no es menor que a (8 < 3 falso)

print("x:", x)
# El resultado es true porque c si es igual a 3.0 (3.0 = 3.0)

