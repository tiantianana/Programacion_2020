# -*- coding: utf-8 -*-
import random


a = int(input("Introducir un número \n"))
b = int(input("Introducir otro número \n"))
c = ((a+5) < b)
print(c)

while c != True:
    print("Incorrecto, Porfavor introducir otros números distintos")
    a = int(input("Introducir un número \n"))
    b = int(input("Introducir otro número \n"))
    c = ((a+5) < b)
    continue
    
for i in range(5):
   
    if (i%2 == 0) == True:
        r = random.randint(a,b)
        while r%2 != 0 :
            r = random.randint(a,b)
        print(r)  
            
    else :
        r = random.randint(a,b)
        while r%2 == 0 :
            r = random.randint(a,b)
        print(r)
    
  
    
        

    
    
    
    

    