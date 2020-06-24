# -*- coding: utf-8 -*-

nombre = 'Johnny Deep'
edad = 55
altura = 178
peso = 65.4
ojos = 'Marrones'
pelo = 'Castaño'

print("Hablemos de %s." %nombre)
print("Mide %i centímetros." %altura)
print("Pesa %f kilogramos." %peso)
print("De hecho no está nada gordo.")	
print("Tiene ojos %s y pelo %s." % (ojos, pelo))

print("\n")

print("Hablemos de", nombre + ".")
print("Mide", altura, "centímetros.")
print("Pesa", peso, "kilogramos.")
print("De hecho no está nada gordo.")
print("Tiene ojos", ojos, "y pelo", pelo + ".")

"""Existe una diferencia en la salida del código. Esta diferecia es encuentra
en los kilogramos.
En la primera forma de imprimir por pantalla, aparece con un mayor número de 
decimales el float del peso que en la segunda forma, la que vimos en clase"""