# -*- coding: utf-8 -*-

class Persona:

    def __init__(self, nombre, dni, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo= "mujer"
        self.DNI = dni
        self.peso = peso
        self.altura = altura
           
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setEdad(self, edad):
        self.edad = edad
    
    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setDNI(self, dni):
        self.DNI = dni
    
    def calcularLetraDNI(self):
        letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        value = self.DNI % 23
        return letras[value]
    
    def setPeso(self, peso):
        if (self.peso>0 and self.peso<120):
           self.peso = peso
        else:
            self.peso = 0
        
    def setAltura(self, altura):
        if (self.altura>0):
            self.altura = altura
        else:
            self.altura = 0
    
    def __str__(self):
        print("Informacion personal: ")
        print("Nombre: ", self.nombre)
        print("Sexo: ", self.sexo)
        print("Edad: ", self.edad)
        print("DNI: ", self.DNI , "-" , self.calcularLetraDNI())
        print("Peso: ", self.peso)
        print("Altura: ", self.altura)

persona = Persona("Ana", 5465132, 20, 40, 150)
persona.__str__()




    
            
    
    
        