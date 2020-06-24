# -*- coding: utf-8 -*-
class TrianguloRectangulo:
    
    def __init__(self, base, altura):
        if(base>0 and altura>0):
            self.base = base
            self.altura = altura
            
    def area(self):
        return (self.base*self.altura)/2

    def perimetro(self):
        hipotenusa = ((self.base**2)+(self.altura**2))**1/2
        return self.base + self.altura + hipotenusa
            
triangulo = TrianguloRectangulo(int(input("base: ")), int(input("altura: ")))

activar = int(input("0. Calcular el área de un triángulo \n"
                "1. Calcular el perímetro \n"))

    
if(activar == 0):
    print(triangulo.area())
else:
    print(triangulo.perimetro())

    
    
    
    
    
    