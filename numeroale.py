#import random
from random import randint
num_alea = randint(1,100)


'''
VARIABLE DE ENTRADA 
nombre     tipo 
numero     int 

VARIABLE SALIDA 
intentos    int       contador 

VARIABLE DE CONTROL 
numero      int
'''
intentos = 0 
#numero = -1
while True: #numero != num_alea: 
    numero= int(input("Adivina el numero oculto entre 1 y 100: "))
    intentos += 1
    if numero > num_alea: 
        print("el numero oculto es menor")
    elif numero < num_alea: 
        print("el numero oculto es mayor")
    else: 
        print("adivinaste")
        break

print(f"NUMERO DE INTENTOS {intentos}")