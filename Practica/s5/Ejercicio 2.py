dinero = 100
pin = 1234

print ("Introduzca el pin")
x = int(input())

if x != pin :
    for i in range(2):
        x = int(input("Introduce el pin \n"))
        if i == 1 and x != pin:
            print ("Se ha agotado el número de intentos")
        elif x == pin:
            print ("pin correcto")  
            print (" 1. Ingreso efectivo \n 2. Retirada efectivo \n 3. Salir")
            y = int(input("Indique la operación a realizar \n"))
            if y == 1:
                ingresar = int(input("Cuanto dinero quiere ingresar?"))
                dinero += ingresar
                print(dinero)
            elif y == 2:   
                retirar = int(input("Cuanto dinero quiere ingresar?"))
                dinero -= retirar
                print(dinero)
            else :
                print("Gracias por confiar en nosotros")
        break
else:
    print ("pin correcto")
    print (" 1. Ingreso efectivo \n 2. Retirada efectivo \n 3. Salir")
    y = int(input("Indique la operación a realizar \n")) 
    if y == 1:
        ingresar = int(input("Cuanto dinero quiere ingresar?"))
        dinero += ingresar
        print(dinero)
    elif y == 2:
        retirar = int(input("Cuanto dinero quiere ingresar?"))
        dinero -= retirar
        print(dinero)
    else :
        print("Gracias por confiar en nosotros")


