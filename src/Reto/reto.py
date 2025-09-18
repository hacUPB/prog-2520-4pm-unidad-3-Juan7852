import calculos as cd 

control = True
while control == True: #while true: bucle infinito para salir break
    print( "1. Evalúa si la pista disponible permite el despegue según masa, temperatura y penalización operativa.\n2. Monitoreo de altitud con detección de tendencias y cálculo de parámetros.\n3. Control de presiones de cabina con detección de fallas y cálculo de parámetros.\n4. Salir")
    opcion=int(input("ingrese una opcion: "))
    match opcion: 
        case 1: 
            # Entradas
            print("Para iniciar los calculos de verificacion de pista ingrese los siguientes datos ")
            masa = float(input("1.Ingrese masa [ton]: "))
            l_disp = float(input("2.Ingrese longitud disponible de pista [m]: "))
            deltaT = float(input("3.Ingrese exceso de temperatura (delta Temperatura) [°C]: "))
            penal = float(input("4.Ingrese penalización operativa [m]: "))
            # Validación
            if masa <= 0 or l_disp <= 0 or penal <= 0:
                print("Error en parámetros")
            else:
                # Cálculos usando las funciones
                lreq_base = cd.calc_lreq_base(masa)
                lreq_aj = cd.calc_lreq_aj(lreq_base, deltaT)
                leff = cd.calc_leff(l_disp, penal)
                mensaje = cd.verificar_pista(leff, lreq_aj)
                #Salida
                print(f"Longitud base requerida: {lreq_base:} m")
                print(f"Longitud ajustada requerida: {lreq_aj:} m")
                print(f"Longitud efectiva disponible: {leff:} m")
                print(f"Resultado: {mensaje}")
        case 2: 
            print("Para iniciar los calculos de monitoreo de altitud ingrese los siguites datos ")
            # Constantes
            intervalo = 20
            duracion = 120
            n_meds = 7
            # Entradas
            alt0 = float(input("Altitud en t=0   [m]: "))
            alt1 = float(input("Altitud en t=20  [m]: "))
            alt2 = float(input("Altitud en t=40  [m]: "))
            alt3 = float(input("Altitud en t=60  [m]: "))
            alt4 = float(input("Altitud en t=80  [m]: "))
            alt5 = float(input("Altitud en t=100 [m]: "))
            alt6 = float(input("Altitud en t=120 [m]: "))
            # Inicializaciones y extremos
            ascensos = 0
            descensos = 0
            alt_min = alt0
            alt_max = alt0 
            # Comparaciones consecutivas usando la función, se utilizo AI para ayuda de comparaciones
            ascensos, descensos, alt_min, alt_max = cd.actualizar_contadores_y_extremos(alt0, alt1, ascensos, descensos, alt_min, alt_max)
            ascensos, descensos, alt_min, alt_max = cd.actualizar_contadores_y_extremos(alt1, alt2, ascensos, descensos, alt_min, alt_max)
            ascensos, descensos, alt_min, alt_max = cd.actualizar_contadores_y_extremos(alt2, alt3, ascensos, descensos, alt_min, alt_max)
            ascensos, descensos, alt_min, alt_max = cd.actualizar_contadores_y_extremos(alt3, alt4, ascensos, descensos, alt_min, alt_max)
            ascensos, descensos, alt_min, alt_max = cd.actualizar_contadores_y_extremos(alt4, alt5, ascensos, descensos, alt_min, alt_max)
            ascensos, descensos, alt_min, alt_max = cd.actualizar_contadores_y_extremos(alt5, alt6, ascensos, descensos, alt_min, alt_max)
            # Calcular promedio
            alt_prom = cd.promedio7(alt0, alt1, alt2, alt3, alt4, alt5, alt6)
            # Salida
            print(f"\nResultados ({n_meds} mediciones, cada {intervalo} min, duración {duracion} min):")
            print(f"Ascensos:  {ascensos}")
            print(f"Descensos: {descensos}")
            print(f"Altitud mínima:  {alt_min:} m")
            print(f"Altitud máxima:  {alt_max:} m")
            print(f"Altitud promedio:{alt_prom:} m")

        case 3: 
            print("Para iniciar los calculos de control de presion ingrese los siguientes datos ")
            # Entradas (6 lecturas: 20→120 min)
            p1 = float(input("presion1 (t=20 min)  [kPa]: "))
            p2 = float(input("presion2 (t=40 min)  [kPa]: "))
            p3 = float(input("presion3 (t=60 min)  [kPa]: "))
            p4 = float(input("presion4 (t=80 min)  [kPa]: "))
            p5 = float(input("ppresion5 (t=100 min) [kPa]: "))
            p6 = float(input("ppresion6 (t=120 min) [kPa]: "))
            # Inicializaciones
            fuera_total_min = 0
            racha_act = 0
            racha_max = 0
            fugas = 0

            p_min = p1
            p_max = p1
            suma  = p1
            # p1: fuera/racha/extremos, se utilizo AI para los diferentes P 
            fuera_total_min, racha_act, racha_max = cd.actualizar_fuera_y_racha(p1, fuera_total_min, racha_act, racha_max)

            # ---- p2 ----
            suma += p2
            p_min, p_max = cd.actualizar_extremos(p2, p_min, p_max)
            fuera_total_min, racha_act, racha_max = cd.actualizar_fuera_y_racha(p2, fuera_total_min, racha_act, racha_max)
            fugas = cd.detectar_salto(p1, p2, fugas)

            # ---- p3 ----
            suma += p3
            p_min, p_max = cd.actualizar_extremos(p3, p_min, p_max)
            fuera_total_min, racha_act, racha_max = cd.actualizar_fuera_y_racha(p3, fuera_total_min, racha_act, racha_max)
            fugas = cd.detectar_salto(p2, p3, fugas)

            # ---- p4 ----
            suma += p4
            p_min, p_max = cd.actualizar_extremos(p4, p_min, p_max)
            fuera_total_min, racha_act, racha_max = cd.actualizar_fuera_y_racha(p4, fuera_total_min, racha_act, racha_max)
            fugas = cd.detectar_salto(p3, p4, fugas)

            # ---- p5 ----
            suma += p5
            p_min, p_max = cd.actualizar_extremos(p5, p_min, p_max)
            fuera_total_min, racha_act, racha_max = cd.actualizar_fuera_y_racha(p5, fuera_total_min, racha_act, racha_max)
            fugas = cd.detectar_salto(p4, p5, fugas)

            # ---- p6 ----
            suma += p6
            p_min, p_max = cd.actualizar_extremos(p6, p_min, p_max)
            fuera_total_min, racha_act, racha_max = cd.actualizar_fuera_y_racha(p6, fuera_total_min, racha_act, racha_max)
            fugas = cd.detectar_salto(p5, p6, fugas)

            # Promedio
            p_prom = cd.promedio6(p1, p2, p3, p4, p5, p6)
            
            # Mensajes
            mensaje = cd.mensaje_final(fuera_total_min)
            aviso   = cd.aviso_fuga(fugas)
            
            # Salida
            print("\n--- Resultados presurización ---")
            print(f"p_min (kPa): {p_min:}")
            print(f"p_max (kPa): {p_max:}")
            print(f"p_prom (kPa): {p_prom:}")
            print(f"Tiempo fuera de rango (min): {fuera_total_min}")
            print(f"Racha fuera de rango más larga (lecturas): {racha_max}")
            print(f"Fugas (saltos > {cd.dP_lim: } kPa): {fugas}")
            print(aviso)
            print(mensaje)
        case 4: 
            control = False
        case _:
            print("opcion invalida")
