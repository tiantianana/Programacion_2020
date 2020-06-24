# -*- coding: utf-8 -*-


print("Introduce una coordenada x")
x = int(input())

print("Introduce una coordenada y")
y = int(input())

if x>0 and y>0 :
    print("Las coordenadas se encuentran en el primer cuadrante")
elif x<0 and y>0 :
	print("Las coordenadas se encuentran en el segundo cuadrante")
elif x<0 and y<0 :
	print("Las coordenadas se encuentran en el tercer cuadrante")
else:
	print("Las coordenadas se encuentran en el cuarto cuadrante")