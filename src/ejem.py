''''
numero1 =int(input("ingrease num1: ")) 
numero2 =int(input("ingrese num2: "))
if numero1 > numero2: 
    mayor= numero1
    menor= numero2
else:
    mayor= numero2
    menor= numero1
while menor <= mayor:
    if menor % 2 ==1:
        print(menor)
    menor += 1      #numero = numero + 1
'''
#solicitar dos numeros y imprimir los impares, acendente  
''''
num = 0
while num <=100:
    if num % 7 == 0:
        print(num)
    num += 1
'''
numero =int(input("ingrease num: ")) 
i = 1 
while i <= 15:
    resultado= i*numero
    print (f"{numero}*{i}={resultado}")
    i += 1
