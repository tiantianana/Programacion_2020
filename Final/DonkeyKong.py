# -*- coding: utf-8 -*-
import pyxel
import random

class Rampas:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.array_rampa = []
        
    def crearRampas(self): 
        
        for x in range(7):      
           #rampa[0] comienzo
            if (x == 0):
                for i in range(14):
                    if(i==0):
                        self.x = 0
                        self.y =248
                        self.array_rampa[:0] = [(self.x,self.y)] 
                        
                    elif(i<8 and i>0):
                        self.x += 16
                        self.array_rampa[:0] = [(self.x,self.y)]
                    else:
                        self.x += 16
                        self.y -=1
                        self.array_rampa[:0] = [(self.x,self.y)]   
            
            #rampa[1] derecha
            elif(x==1):
                for j in range(14):
                    if(j==0):
                        self.x=-16
                        self.y=208
                    else:
                        self.x += 16
                        self.y +=1
                        self.array_rampa[:0] = [(self.x,self.y)]
                    
           #rampa[2] izq
            elif(x==2):
                for i in range(14):
                    if(i==0):
                        self.x=224
                        self.y=176
                    else:
                        self.x -= 16
                        self.y +=1
                        self.array_rampa[:0] = [(self.x,self.y)]
                    
                    #rampa[3] drcha
            elif (x==3):
                for i in range(14):
                    if(i==0):
                        self.x=-16
                        self.y=144
                    else:
                        self.x += 16
                        self.y +=1
                        self.array_rampa[:0] = [(self.x,self.y)]
                            
                    #rampa[4] izq
            elif (x==4):
                for i in range(14):
                    if(i==0):
                        self.x=224
                        self.y=112
                    else:
                        self.x -= 16
                        self.y +=1
                        self.array_rampa[:0] = [(self.x,self.y)]
                            
                    #rampa[5] drcha 
            elif (x==5):
                for i in range(13):
                    if(i==0):
                        self.x=0
                        self.y=88
                        self.array_rampa[:0] = [(self.x,self.y)]
                    elif(i<9 and i>0):
                        self.x += 16
                        self.array_rampa[:0] = [(self.x,self.y)]
                    else:
                        self.x += 16
                        self.y +=1
                        self.array_rampa[:0] = [(self.x,self.y)]
            elif (x==6):
                for i in range(3):
                    if(i==0):
                        self.x=88
                        self.y=56
                        self.array_rampa[:0] = [(self.x,self.y)]                    
                    else:
                        self.x +=16
                        self.array_rampa[:0] = [(self.x,self.y)] 

    
class Escaleras:
    def __init__(self, x, y, h):
        self.pos_escalera_x = x
        self.pos_escalera_y = y
        self.escalera_h = h
        self.lista_escalera = []
        
    def crearEscaleras(self):
        
        for i in range(4):
            #Creamos el primer tramo de escaleras, las situadas en la parte superior junto a Donkey Kong
            if i == 0: 
                #Según el tramo de escaleras con el que trabajamos, inicializamos valores distintos para las posiciones y la altura
                for i in range(4):
                    self.pos_escalera_x = 78
                    self.escalera_h = 16
                    #Aprovechamos a añadir varias escaleras al mismo tiempo a la listapara ahorrar espacio 
                    if(i == 0):
                        self.pos_escalera_y = 32
                        self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x - 18, self.pos_escalera_y, self.escalera_h)]
                    elif(i==1):
                        self.pos_escalera_y += 16
                        self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x - 18, self.pos_escalera_y, self.escalera_h)]
                    elif(i==2):
                        self.pos_escalera_y += 16
                        self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x - 18, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x + 48, self.pos_escalera_y, self.escalera_h)]
                    elif(i==3):
                        self.escalera_h = 8
                        self.pos_escalera_y += 16
                        self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x - 18, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x + 48, self.pos_escalera_y, self.escalera_h)]
           
            #A continuación, las escaleras que están en las posiciones de menor y mayor "x" de todas, que coincidentemente estan alineadas en el eye "y"
            if i == 1:
                self.pos_escalera_x = 182
                self.pos_escalera_y = 228
                self.escalera_h = 16
                self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h),(self.pos_escalera_x - 150, self.pos_escalera_y - 32, self.escalera_h), (self.pos_escalera_x, self.pos_escalera_y - 65, self.escalera_h)] 
                self.lista_escalera[:0] = [(self.pos_escalera_x - 150, self.pos_escalera_y - 97, self.escalera_h), (self.pos_escalera_x, self.pos_escalera_y - 129, self.escalera_h)]
          
            #Estas son las últimas escaleras que no están rotas, que son de mayor tamaño     
            if i == 2:
                for i in range(2):
                    self.pos_escalera_x = 70
                    self.escalera_h = 16
                    if(i == 0):
                        self.pos_escalera_y = 130
                        self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h),(self.pos_escalera_x, self.pos_escalera_y + 4, self.escalera_h)]
                    elif(i==1): 
                        self.pos_escalera_x += 26
                        self.pos_escalera_y += 62
                        self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h),(self.pos_escalera_x, self.pos_escalera_y + 8, self.escalera_h), (self.pos_escalera_x + 16, self.pos_escalera_y - 32, self.escalera_h), (self.pos_escalera_x + 16, self.pos_escalera_y - 24, self.escalera_h)]
          #Y aquí las últimas escaleras, las escaleras rotas
            if i == 3:
               for i in range(2): 
                   if (i == 0): #La parte de arriba de las escaleras partidas
                       self.pos_escalera_x = 88
                       self.pos_escalera_y = 96
                       self.escalera_h = 5
                       self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h), (self.pos_escalera_x -24, self.pos_escalera_y + 59, self.escalera_h + 3), (self.pos_escalera_x -8, self.pos_escalera_y +125, self.escalera_h -1), (self.pos_escalera_x +78, self.pos_escalera_y +28, self.escalera_h +3)]
                   if (i == 1): #La parte de abajo de las escaleras partidas
                       self.pos_escalera_x = 88
                       self.pos_escalera_y = 108
                       self.escalera_h = 9
                       self.lista_escalera[:0] = [(self.pos_escalera_x, self.pos_escalera_y, self.escalera_h +4),(self.pos_escalera_x -24, self.pos_escalera_y + 70, self.escalera_h), (self.pos_escalera_x -8, self.pos_escalera_y +132, self.escalera_h), (self.pos_escalera_x +78, self.pos_escalera_y +38, self.escalera_h)]
             

class DK:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contador = 0
    #Las posiciones para la x e y se definen en la clase App
    
    def aparecer(self):
        self.contador = 0
        
        if pyxel.frame_count % 180 >= 60:
            self.contador += 1
        
        #Si el contador es 1 se pone la imagen normal de DK
        if self.contador == 1:
            pyxel.blt(self.x, self.y, 1, 150, 8, 50, 32, 3)    
        
        #Si el contador es 0 cambia la imagen de DK
        else :
            pyxel.blt(self.x, self.y, 1, 4, 7, 40, 32, 3)
    
            
#Pauline se mantendrá siempre en la misma posición
class Pauline: 
    def __init__(self, x, y):
        self.pauline_x = x
        self.pauline_y = y
        self.contador = 0
        
    #Las posiciones para la x e y se definen en la clase App
    def aparecer(self):
        self.contador = 0
        
        if pyxel.frame_count % 260 >= 60:
            self.contador += 1
        
        if self.contador == 1:
            pyxel.blt(self.pauline_x, self.pauline_y, 0, 2, 230, 15, 22, 3)
            
        else :
            pyxel.blt(110, 33, 0, 2, 197, 20, 15, 3)
            pyxel.blt(self.pauline_x, self.pauline_y, 0, 26, 230, 15, 22, 3)
  
                      
class Mario:
    def __init__(self, x, y, vidas):
        self.mario_x = x
        self.mario_y = y
        self.vidasMario = vidas
        self.array_rampa = []
        
    def aparecer(self): 
    #Depende de la tecla que pulse el jugador, aparecerá un Sprite diferente de Mario
        if pyxel.btn(pyxel.KEY_RIGHT): 
            return pyxel.blt(self.mario_x, self.mario_y, 0, 218, 20, 12, 16, 3)
        
        if pyxel.btn(pyxel.KEY_LEFT):
            return pyxel.blt(self.mario_x, self.mario_y, 0, 24, 0, 12, 16, 3)
        
        if pyxel.btn(pyxel.KEY_UP):
            #Si solo se toca la tecla para subir (EJ. subir una escalera)
            return pyxel.blt(self.mario_x, self.mario_y, 0, 98, 20, 12, 16, 3)
        else:
            #Si pulsa junto a otra tecla, para saltar un obstáculo
            return pyxel.blt(self.mario_x, self.mario_y, 0, 242, 20, 12, 16, 3)
        
    def numVidas(self): 
        #Determinamos las vidas de Mario (3 son las iniciales)
        self.vidas_x = 0
        self.vidas_y = 24
        lista_vidas = []
        for i in range(self.vidasMario):
            self.vidas_x += 8
            lista_vidas[:0] = [(self.vidas_x, self.vidas_y)]
        return lista_vidas
      
    def toparEscalera(self, escaleras):
        HayEscalera = False
        #Si encuentra una escalera, Mario puede subir
        for i in range(0, len(escaleras.lista_escalera)):
            escalera = escaleras.lista_escalera[i]
            # Si Mario se encuentra en una escalera (en intervalo de escalera - 6 y escalera + 6 ya que Mario tiene 12 de anchura)
            # Lo mismo ocurre con la y de Mario, como mario mide 16 utilizamos una rango de -8 y 8
            # La altura 10 es para que Mario no pueda subir las escaleras rotas
            if self.mario_x in range(escalera[0] - 6, escalera[0] + 6) and self.mario_y in range(escalera[1]- 8, escalera[1] + 10) and escalera[2] > 10:
                HayEscalera = True
        return HayEscalera
    
    def hayRampa(self, rampas):
        HayRampa = False
        for i in range(0, len(rampas.array_rampa)):
                rampa = rampas.array_rampa[i]
                #La y de Mario tiene un rango de la rampa y 4 (ya que es la altura de la rampa)
                if (self.mario_x + 12) in range(rampa[0], rampa[0] + 20) and self.mario_y in range(rampa[1], rampa[1]+ 4):
                    HayRampa == True
        return HayRampa
    
    def mover(self, rampas, escaleras): 
        #Llamamos a los métdos toparEscalera y hayRampa, asignando variables booleanas correspondientes
        HayEscalera = self.toparEscalera(escaleras)
        HayRampa = self.hayRampa(rampas)
        #Si encuentra una escalera, Mario puede subir
            
        #Pulsando el boton derecho Mario se desplaza, hay que tener en cuenta que la rampa es inclinada
        if pyxel.btn(pyxel.KEY_RIGHT) and self.mario_x < 212:
            self.mario_x += 1
            # Recorremos la lista hasta la ultima rampa (longitud del array rampa = 80)
            for i in range(0, len(rampas.array_rampa)):
                #Guardamos cada posicion en la variable rampa
                rampa = rampas.array_rampa[i]
                # la rampa[0] es la componente x y la rampa[1] es la componente y de la rampa
                
                #Comprobamos que Mario esta dentro de una rampa (con el eje x)
                #Comprobamos que la siguiente rampa esta más alta que mario (por tanto ha de subir), en caso contrario, Mario avanza libremente
                if (self.mario_x + 12) in range(rampa[0], rampa[0] + 16) and rampa[1] in range(self.mario_y, self.mario_y +16):
                    self.mario_y -=1
                    
                # En caso de que no se cumpla el primer caso, es posible que Mario este bajando. Por tanto vemos si Mario tiene una rampa por debajo.
                elif (self.mario_x + 12) in range(rampa[0], rampa[0] + 16) and rampa[1] in range(self.mario_y +17, self.mario_y + 24):
                    self.mario_y += 1

        #Si no se cumple ninguno de los casos es que la rampa no tiene inclinacion y Mario avanza libremente
                
        #Ocurre lo mismo si apretamos el boton de la izquierda, la diferencia es que mario se mueve al lado contrario
        if pyxel.btn(pyxel.KEY_LEFT) and self.mario_x > 0:
            self.mario_x -= 1         
            # recorremos la lista hasta la ultima rampa
            for i in range(0, len(rampas.array_rampa)):
                rampa = rampas.array_rampa[i]
                # rampa[0] + 16 (rampa x mas su longitud)
                # self.y + 16 (Mario mas su altura)
                if (self.mario_x + 12) in range(rampa[0], rampa[0] + 16) and rampa[1] in range(self.mario_y, self.mario_y +16):
                    self.mario_y -=1
                   
                # si Mario esta entre las medidas de la rampa
                elif (self.mario_x + 12) in range(rampa[0], rampa[0] + 16) and rampa[1] in range(self.mario_y +17, self.mario_y + 24):
                    self.mario_y += 1
                         
        #Mario puede subir pero unicamente por las escaleras
        if pyxel.btn(pyxel.KEY_UP) and self.mario_y > 0:
            self.mario_y -= 2
            if (HayEscalera == False and HayRampa == True):
                #Si no hay escalera pero sí una plataforma, entonces Mario no puede atravesar la rampa
                    self.mario_y = rampa[1] + 4
                    
        #Mario puede saltar y caer por la accion de la gravedad
        if pyxel.btn(pyxel.KEY_SPACE) and self.mario_y > 0:
            self.mario_y -= 3
            
            #Si Mario encuentra una rampa por encima, no puede atravesarla por lo que no puede seguir avanzando y baja     
            for i in range(0, len(rampas.array_rampa)):
                rampa = rampas.array_rampa[i]
                #La y de Mario tiene un rango de la rampa y 4 (ya que es la altura de la rampa)
                if (self.mario_x + 12) in range(rampa[0], rampa[0] + 20) and self.mario_y in range(rampa[1], rampa[1]+ 4):
                    self.mario_y = rampa[1] + 4
                    
        #La accion de la gravedad hace que si no hay escalera Mario puede bajar hasta que pisa una plataforma
        if self.mario_y < 232:
            if not HayEscalera:
                self.mario_y += 1
            
                #Este bucle indica a Mario que ha llegado a la plataforma y que no puede bajar mas  
                for i in range(0, len(rampas.array_rampa)):
                    rampa = rampas.array_rampa[i]
                    if (self.mario_x + 12) in range(rampa[0], rampa[0] + 20) and rampa[1] in range(self.mario_y + 14, self.mario_y+ 18):
                        self.mario_y = rampa[1] - 16

#Creamos una clase lista de barriles donde se almacenan los barriles que aparecen en pantallan. Estos pueden bajar la rampa o las escaleras
class Lista_barriles:
    def __init__(self):
        self.barriles = []
        self.contador = 0
     
    # Crea una lista de objetos donde se guarda como maximo 10 barriles         
    def crearBarril(self):
        
        #Sirve para determinar a que velocidad aparecen los barriles. En mi caso hemos escogido 180, que es cada 3 segundos
        if pyxel.frame_count % 180 == 0:
            self.contador += 1
        
        if self.contador == 1:
            #Creamos objetos de tipo barril
            self.barril = Barril(70, 78)
                        
            if len(self.barriles) <= 10:  
                #Anadimos cada barril a la lista barriles []
                self.barriles.append(self.barril)
                self.contador = 0
                
                #Como solo pueden aparecer 10 barriles, eliminamos el barril de la primera posicion para asi dejar espacio en la lista y poder introducir el nuevo barril
                if len(self.barriles) == 10:
                    del self.barriles[1]
                    
    #Esta es una funcion que recorre la lista de barriles y asi aparece cada barril
    def aparecer(self): 
        for b in self.barriles:
            b.aparecer()
        
        #Creamos cada barril
        self.crearBarril()
     
    #La funcion roda hace que cada barril por separado (recorre la lista de barriles) pueda desplazarse a lo largo de la rampa y caer por las escaleras
    def rodar(self, rampas, escaleras):
        for b in self.barriles:
            b.rodar(rampas, escaleras)
                                     
class Barril:
    def __init__(self, x, y):
        self.pos_barril_x = x
        self.pos_barril_y = y
    
    #Aparecen los barriles y desaparecen cuando estan en la posicion 0, es decir cuando ha terminado de bajar la rampa
    def aparecer(self):
        if (self.pos_barril_x > 0 and self.pos_barril_y < 245):
            return pyxel.blt(self.pos_barril_x, self.pos_barril_y, 0, 59, 118, 12, 12, 3)
        
    def hayRampa(self, rampas):
         HayRampa = False
          #Comprobamos si hay rampa debajo del barril
         for i in range(0, len(rampas.array_rampa)):
             rampa = rampas.array_rampa[i]
             # En la y del barril, comprobamos en un intervalo de -4 y +4 ya que hacen un total de 8, que es la altura de la rampa
             if self.pos_barril_x in range(rampa[0]- 12, rampa[0] + 16) and self.pos_barril_y +12 in range(rampa[1] - 4, rampa[1] +4):
                 HayRampa = True
                 
         return HayRampa
        
    def hayEscalera(self, escaleras):
        HayEscalera = False
        #Metodo para encontrar una escalera y que el barril pueda bajarla
        for i in range(0, len(escaleras.lista_escalera)):
            escalera = escaleras.lista_escalera[i]
            # Ponemos el rango de la x del barril entre la x de la escalera y la x + 10 ya que es la anchura de la escalera
            # Ponemos que la y del barril este en el rango de la escalera - 20 (altura del barril +12 +4 de la altura de la escalera + 2 de margen y la y de la escalera)
            # Hacemos que la altura de la escalera sea mayor que 10 (pues solo puede bajar por las verdaderas escaleras y no aquellas que estan cortadas)
            if self.pos_barril_x in range(escalera[0], escalera[0] + 10) and self.pos_barril_y in range (escalera[1]- 20, escalera[1]) and escalera[2] > 10:
                HayEscalera = True
                  
        return HayEscalera
            
    def rodar(self, rampas, escaleras):
        #Llamamos a los métdos toparEscalera y hayRampa, asignando variables booleanas correspondientes
        HayEscalera = self.hayEscalera(escaleras)
        HayRampa = self.hayRampa(rampas)
        #Creamos una variable nueva con la librería random para comprobar con posterioridad si el barril desciede o no
        esBajar = random.randint(0, 99)
        
        if (self.pos_barril_x > 0 and self.pos_barril_x < 222):
            #Tenemos varias opciones, que ruede si debajo tiene una rampa o que caiga si debajo no hay rampa, 
            # o que baje or una escalera 
            
            if esBajar > 25: 
            #En caso de que no se vaya a bajar, se ignora la existencia de la escalera
                HayEscalera = False 
                
            if HayEscalera == True:
                #En caso de que si baje por la escalera, desciende un cierto número de unidades
                self.pos_barril_y += 1
            
            if HayRampa == True and HayEscalera == False:
                self.pos_barril_x += 1 
                
                #EL BARRIL BAJA LA RAMPA (INCLINADO)
                for i in range(0, len(rampas.array_rampa)):
                    rampa = rampas.array_rampa[i]
                    
                    if (self.pos_barril_x + 12) in range(rampa[0], rampa[0] + 16) and rampa[1] in range(self.pos_barril_y + 10, self.pos_barril_y+ 18):
                        self.pos_barril_y = rampa[1] - 12
                        
                        #Cambio de sentido
                        if self.pos_barril_y in range(101, 134) or self.pos_barril_y in range(165, 180) or self.pos_barril_y in range(228, 248):
                            self.pos_barril_x -= 2 
                              
            #Baja si no encuentra ninguna rampa
            elif HayRampa == False:
                self.pos_barril_y += 2

            
class App:
    def __init__(self):
        #Dimensiones y nombre que tiene la pantalla de juego
        pyxel.init(224, 256, caption="Donkey Kong")
        #Cargamos el archivo de donde sacamos los sprites para el juego
        pyxel.load("Sprites.pyxres")
        
        self.reset()
        pyxel.run(self.update, self.draw)
        
    #Método creado para que se resetee la pantalla a estos valores iniciales cada vez que se ejecuta el código:
    def reset(self):
        #Damos los parámetros iniciales de posición x  e y a Donkey kong, Mario y Pauline
        self.DonkeyKong = DK(20, 56)
        self.mario = Mario(56, 232, 3)
        self.pauline = Pauline(88, 33) 
        #Para las plataformas, escaleras y barriles, las iniciallizamos a cero puesto a que sus métodos propios son los que les otrogan las posiciones
        self.EsRampas = Rampas(0, 0)
        self.EsRampas.crearRampas()
        
        self.EsEscaleras = Escaleras(0, 0, 0)
        self.EsEscaleras.crearEscaleras() 
           
        self.listabarriles = Lista_barriles()
        self.listabarriles.crearBarril()

        
    def update(self):
        #Con este método actualizamos en cada frame la pantalla
        self.vidas = []
        self.lista_escaleras = []
        self.lista_barriles = []
        #Y actualizamos el movimento de Mario y los barriles
        self.mario.mover(self.EsRampas, self.EsEscaleras)
        self.listabarriles.rodar(self.EsRampas, self.EsEscaleras)
        
        
    def draw(self):
        pyxel.cls(0)
        #Posicionamos a los personajes en sus posiciomes iniciales
        self.pauline.aparecer() #Pauline
        #self.DonkeyKong.posInicial() #DK 
        self.mario.aparecer() #Mario
        self.DonkeyKong.aparecer()

        #Creamos las escaleras:
        for self.pos_escalera_x,self.pos_escalera_y,self.escalera_h in self.EsEscaleras.lista_escalera:
            pyxel.blt(self.pos_escalera_x, self.pos_escalera_y, 0, 121, 237, 10, self.escalera_h, 3)
        #Creamos las rampas:
        for self.x,self.y in self.EsRampas.array_rampa:
            pyxel.blt(self.x, self.y, 0, 236, 103, 16, 8, 3)
        #Barriles fijos
        pyxel.blt(0, 56, 0, 3, 99, 20, 32, 3)
        
        #Para los barriles que no son estáticos, hacemos que empiezen a aparecer cuando los frames lleguen a 65
        if(pyxel.frame_count > 65):
            self.listabarriles.aparecer()
        
        #Creamos los sprites para las vidas
        for self.vidas_x, self.vidas_y in self.mario.numVidas():
            pyxel.blt(self.vidas_x, self.vidas_y, 0, 241, 201, 8, 8, 3)
            
        #Puntuación actual del jugador:
        pyxel.text(8, 8, "000000", 7) 
        #Puntuación máxima obtenida por el jugador:
        pyxel.text(88, 0, "HIGH SCORE:", 8)
        pyxel.text(96, 8, "000000", 7)
        #Nivel en el que se encuentra el jugador 
        pyxel.text(168, 24, "L = 01", 1)
        
App() #Cargamos la aplicación (El juego)


