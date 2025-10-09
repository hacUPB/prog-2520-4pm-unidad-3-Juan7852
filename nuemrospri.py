numero= int(input("ingresa un numero entero mayor que 1: "))
divisor= numero//2
contador= 0
for i in range(2,divisor+1):
    if numero % i == 0: 
        contador+=1



if contador ==0:
    print( f"el numero {numero} es primo")
else: 
    print(f"el numero {numero}no es primo ")
    print("los divisores son: ")
    for i in range (1, numero+1):
        if numero % i == 0: 
            print(i)
      
