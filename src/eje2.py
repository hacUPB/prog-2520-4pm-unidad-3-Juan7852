#determinar si un numero es par o impar 
numero = int(input( "ingrese un numero: "))
residuo = numero % 2
if residuo == 0:
    print ("el numero es par")
else: 
    print ( "el nuemro es impar")
    