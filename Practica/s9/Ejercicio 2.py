# -*- coding: utf-8 -*-

class Rectángulo:
    Base = 0
    Altura = 0
    Is_Cuadrado = False
   
    def setBase(self, base):
        self.Base = base
    
    def setAltura(self, altura):
        self.Altura = altura
        
    def setIsCuadrado(self, isCuadrado):
        self.Is_Cuadrado = isCuadrado
    
    def getBase(self):
        if(self.Base < 0): return 0
        return self.Base
    
    def getAltura(self):
        if(self.Altura < 0): return 0
        return self.Altura
    
    def getIsCuadrado(self):
        if(self.getAltura() == self.getBase()): 
            self.Is_Cuadrado = True
        return self.Is_Cuadrado
    
    def __init__(self, base, altura, isCuadrado = False):
       self.Base =  base
       self.Altura = altura
       self.Is_Cuadrado = isCuadrado
       if(self.getBase() == 0):
           isCuadrado = True
           base == altura

       if(self.getAltura() == 0):
           isCuadrado = True
           altura == base

    def str_(self):
        datos = " "
        if (self.getIsCuadrado() == True):
            datos = ("Un cuadrado de base ", self.getBase(), "y altura", self.getAltura())
        else: 
            datos = ("Un rectángulo de base ", self.getBase(), "y altura",self.getAltura())
        return datos
        
    def eq(rec1, rec2):
        if(rec1.getBase() == rec2.getAltura() and rec1.getAltura() == rec2.getBase()):
            return True
        else: return False

    def perimetro(self):
        perimetro = (self.getBase() * 2) + (self.getAltura() * 2)
        return perimetro
    
    def area(self):
        area = self.getBase() * self.getAltura()
        return area
    
    def ladoMayor(self):
        if(self.getAltura() > self.getBase()):
            return self.getAltura() 
        else: 
            return self.getBase()

    def convertir(self):
        if(self.getBase() < self.getAltura()):
            self.Base = self.Altura
            return True
        
        else:
            self.Altura = self.Base
            return False
        

import random
class Main(Rectángulo):
    rectangulos = []
    a = random.randint(10,1000)
    for i in range(a):
        rectangulos.append(Rectángulo(random.randint(1,10), random.randint(1,10)))

    cuadrados = []
    for i in range(len(rectangulos)):
        if (rectangulos[i].getIsCuadrado() == True):
            cuadrados.append(rectangulos[i])
            print(rectangulos[i].str_())
            
    lado_mayor = []        
    for i in range(len(rectangulos)):
        if(rectangulos[i].getIsCuadrado() == False):
            if (rectangulos[i].getAltura() == 10 or rectangulos[i].getBase() == 10):
                lado_mayor.append(rectangulos[i])
                print(rectangulos[i].str_())
                