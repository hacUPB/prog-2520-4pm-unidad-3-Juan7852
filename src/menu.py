
#utilizamos una variable tipo boleana -> una bandera 
control = True
while control == True: #while true: bucle infinito para salir break
    print( "1. entradas\n2. platos fuertes\n3.bebidas\n4. postres\n5.salir")
    opcion=int(input("ingrese una opcion: "))
    match opcion: 
        case 1: 
            print("1. patacon con hagao")
            print("2. yuca con chicharron")
            print("3. guineo con suero")
            #opc1= int(input("ingrese su eleccion: "))
        case 2: 
            print("1. salomito")
            print("2. hamurguesa")
            print("3. sushi")
        case 3: 
            print("1. limonada")
            print("2. jugos natu")
            print("3. sushi")
        case 4: 
            print("1. tres leches")
            print("2. fresas")
            print("3. sushi")
        case 5: 
            control = False
        case _:
            print("opcion invalida")

