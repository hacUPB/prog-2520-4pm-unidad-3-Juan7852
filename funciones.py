'''
def suma(a, b):
	resultado = a + b
	return resultado


#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

#crear una funcion que imprima la tabla de cualquier numero - bucle for 
def tabla(num):
    for i in range (1,11):
        producto = i * num 
        print(f"{num}x{i}={producto}")
numero = int(input("ingrese el valor: "))
tabla (numero)

funcion: menu 
paramatros de entrada: ninguno
ejecucion: imprimir en pantalla 4 opciones diferentes, solicitar que elija una opcion y la guarda en una variable
valor retorno: opcion elegida 
'''

def menu():
    print("1.Encabezado")
    print("2.porcentaje")
    print("3.mensaje")
    print("4.helado")
    option=int(input("elija una opcion: "))
    return option
def encabezado(mensaje):
    print("juan lasso")
    print("493693")
    print("ing aero")
    return mensaje

def procentaje(a,b):
    a=float(input("Ingrese el valor total: "))
    b=float(input("ingrese el porcentaje: "))
    return b 

def cierre():
    print("game over")

 
eleccion= menu()
match(eleccion):
    case 1: 
        mensaje=input("escribe el mensaje: ")
        encabezado(mensaje)
        #imprimir info sobre uno, parametro:mensaje que imprime dentro de la funcion 
    case 2: 
        procentaje(a,b)
        #parametro 1: valor total
        #parametro 2: porcentaje
        #retorno: valor del porcentaje
    case 3:
        cierre()
        #no recibe ningun parametro y no devuelve un resultado
        #imprime un menaje que cierra el programa