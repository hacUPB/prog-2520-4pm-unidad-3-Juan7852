
nombre = input ("por favor ingrese su nombre: ")
print ("bienvenido " , nombre)

#calcular el indice de masa corporal
#inc: peso/altura
estatura = input ("ingrese estatura en metros ")
estatura = float (estatura)
peso = input ("ingrese su peso en kg ")
peso = float (peso) 
inc = peso / estatura **2
print ("su inc =", inc)
if inc <= 18.49 : 
    print ("peso bajo")
elif inc <= 24.99 : 
    print ("peso normal")
elif inc <= 29.99 : 
    print ("sobrepeso")
elif inc <= 39.99 : 
    print ("obesidad")
else: 
    print ("obesidad extrema")