import calculos as cd 
#utilizamos una variable tipo boleana -> una bandera 
control = True
while control == True: #while true: bucle infinito para salir break
    print( "1. entradas\n2. platos fuertes\n3.bebidas\n4. postres\n5.salir")
    opcion=int(input("ingrese una opcion: "))
    match opcion: 
        case 1: 
            # Entradas
            masa = float(input("Ingrese masa [ton]: "))
            l_disp = float(input("Ingrese longitud disponible de pista [m]: "))
            deltaT = float(input("Ingrese exceso de temperatura (deltaT) [°C]: "))
            penal = float(input("Ingrese penalización operativa [m]: "))
            # Validación
            if masa <= 0 or l_disp <= 0 or penal <= 0:
                print("Error en parámetros")
            else:
                # Cálculos usando las funciones
                lreq_base = cd.calc_lreq_base(masa)
                lreq_aj = cd.calc_lreq_aj(lreq_base, deltaT)
                leff = cd.calc_leff(l_disp, penal)
                mensaje = cd.verificar_pista(leff, lreq_aj)
                #Mostrar resultados
                print(f"Longitud base requerida: {lreq_base:.2f} m")
                print(f"Longitud ajustada requerida: {lreq_aj:.2f} m")
                print(f"Longitud efectiva disponible: {leff:.2f} m")
                print(f"Resultado: {mensaje}")
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

