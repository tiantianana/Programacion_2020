# -*- coding: utf-8 -*-

class Tiempo:
    Hora = 0
    Minutos = 0
    
    def __init__(self, hora, mins):
        self.Hora = hora
        self.Minutos = mins
    
    def setHora(self, hora):
        self.Hora = hora
    
    def setMinutos(self, minutos):
        self.Minutos = minutos
        
    def getHora(self):
        if(self.Hora >= 0 and self.Hora < 24):
            return self.Hora
        else:
            return 0
        
    def getMinutos(self):
        if(self.Minutos >= 0 and self.Minutos < 60):
            return self.Minutos
        else:
            return 0
        
    def IntervaloTemporal(t1, t2):
        return [t1.getHora(),":",t1.getMinutos(),"-",t2.getHora(),":",t2.getMinutos()]
   
    def Pertenencia(t1, t2):
        p = "Pertenece a la "
        if(t1.getHora() < 6):
            p += "madrugada"
            if(t2.getHora() >= 6 and t2.getHora() < 12):
                p += " mañana"
            elif(t2.getHora() >= 12 and t2.getHora() < 18):
                p += " tarde"
            elif(t2.getHora() >= 18):
                p += " noche"
        elif(t1.getHora() >= 6 and t1.getHora() < 12):
            p += "mañana"
            if(t2.getHora() >= 12 and t2.getHora() < 18):
                p += " tarde"
            elif(t2.getHora() >= 18):
                p += " noche"
            elif(t2.getHora() < 6):
                p += " madrugada"
        elif(t1.getHora() >= 12 and t1.getHora() < 18):
            p += "tarde"
            if(t2.getHora() >= 18):
                p += " noche"
            elif(t2.getHora() < 6):
                p += " madrugada"
            elif(t2.getHora() >= 6 and t2.getHora() < 12):
                p += " mañana"
        elif(t1.getHora() >= 18):
            p += "noche"
            if(t2.getHora() < 6):
                p += " madrugada"
            elif(t2.getHora() >= 6 and t2.getHora() < 12):
                p += " mañana"
            elif(t2.getHora() >= 12 and t2.getHora() < 18):
                p += " tarde"
        return p
    
t1 = Tiempo(5, 23)
t2 = Tiempo(18,42)
print(Tiempo.IntervaloTemporal(t1, t2), Tiempo.Pertenencia(t1,t2))   