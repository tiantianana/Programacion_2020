# -*- coding: utf-8 -*-

print("Dime un año")
N = int(input())


if N<= 2019 :
    if N%4 == 0 :
        if N%100 == 0 :
            if N%100 == 0 :
                print("Si fue bisiesto")
            else : print("No fue bisiesto")
        else : print("Si fue bisiesto")
    else: print("No fue bisiesto")
elif N> 2019:
    if N%4 == 0 :
        if N%100 == 0:
            if N%100 == 0: print("Si será bisiesto")
            else : print("No será bisiesto")
        else : print("Si será bisiesto")
    else: print("No será bisiesto")

