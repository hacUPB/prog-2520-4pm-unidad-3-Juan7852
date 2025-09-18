# Ejemplo 3: Control de un modo de operación
modo = 2

match modo:
    case 1:
        print("Modo 1 seleccionado: Alta Tensión")
    case 2:
        print("Modo 2 seleccionado: Media Tensión")
    case 3:
        print("Modo 3 seleccionado: Baja Tensión")
    case _:
        print("Modo no válido")