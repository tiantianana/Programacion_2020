# -*- coding: utf-8 -*-

a, b, c, d = 5, 3, 20, 20
c -= (a+1)/b-3+a%b
d -= (a+1)/(b+3-4*a)%b
print("c:", c)
print("d:", d)

"""
Para sacar el resultado del c, se realizan las siguientes operaciones:
    Primero, se suma a+1, dando 6
    A este resultado se le divide entre b, con lo cual da 2
    A dos se le resta 3, con un resultado de -1
    Al -1 se le suma el resto de dividir a entre b, (5/3) que es 2
    -1 + 2 = 1
    Y este resultado se le resta a c, dando 19 que es lo que aparece por pantalla
    
Para sacar el resultado del d, sin embargo, se siguen los siguientes pasos:
    Primero, se le vuelve a sumar a+1, dando nuevamente 6
    En una operación aparte, se siguen los siguientes pasos:
        Primero se le suma 3 a b, la suma resultando 6
        Después, se le resta 4*a, o 20, dando -14
    Se calcula el resto de dividir 6 entre -14, cuyo valor equivale a (-3/7)
    Con el resto obtenido se le hace el módulo con b, dando 20/7
    Este resultado se le resta a d, dando el 17.425714.. que sale en pantalla
    
"""