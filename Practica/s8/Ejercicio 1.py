class Estudiante:
    
    def __init__ (self, nombre, apellido, nota_programacion, nota_algebra, nota_calculo, nota_fisica, nota_tecnicas, nota_humanidades):
        self.nombre = nombre
        self.apellido = apellido
        if(nota_programacion > 10 or nota_programacion < 0):
            self.nota_programacion = 0
        else: 
            self.nota_programacion = nota_programacion
        if(nota_algebra > 10 or nota_algebra < 0): 
            self.nota_algebra = 0
        else: 
            self.nota_algebra = nota_algebra
        if(nota_calculo > 10 or nota_calculo < 0):
            self.nota_calculo = 0
        else: 
            self.nota_calculo= nota_calculo
        if(nota_fisica > 10 or nota_fisica < 0):
            self.nota_fisica = 0
        else: 
            self.nota_fisica= nota_fisica
        if(nota_tecnicas > 10 or nota_tecnicas < 0):
            self.nota_tecnicas = 0
        else: 
            self.nota_tecnicas= nota_tecnicas
        if(nota_humanidades > 10 or nota_tecnicas < 0):
            self.nota_humanidades = 0
        else: 
            self.nota_humanidades= nota_humanidades
    
    def imprimir(self):
        print("")
        print("Nombre: " ,self.nombre)
        print("Apellido: " ,self.apellido)
        print("nota programacion: " ,self.nota_programacion)
        print("nota algebra: " ,self.nota_algebra)
        print("nota calculo: " ,self.nota_calculo)
        print("nota fisica: " ,self.nota_fisica) 
        print("nota tecnicas: " ,self.nota_tecnicas)
        print("nota humanidades: " ,self.nota_humanidades)
        
        
estudiante = Estudiante(input("Nombre: "), input("Apellido: "), int(input("nota programacion: ")), int(input("nota algebra: ")), int(input("nota_calculo: ")), int(input("nota_fisica: ")), int(input("nota_tecnicas: ")), int(input("nota_humanidades: ")))
estudiante.imprimir()