# -*- coding: utf-8 -*-

A = 5
B = 0
"""C = A/B"""

"""SE produce un fallo.
Aparece un error en la pantalla puesto a que no se puede dividir un número
entre 0"""

A2 = 5 + 7j
B2 = 0 + 2j
C2 = A2/B2

"""En este caso la variable C2 es calculada si existe la parte imaginaria de 
la variable B2.
En caso de que no exsita dicha parte, el programa volverá a dar un error"""