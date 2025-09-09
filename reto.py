'''
1. Verificar si la longitud de pista disponible es suficiente para el despegue en función de la masa del avión.
2. Registrar la altitud de vuelo cada 20 minutos durante dos horas y mostrar todas las mediciones al final.
3. ⁠Registrar la presión de cabina cada 10 minutos durante 1 hora y comprobar en cada medición si se mantiene dentro del rango seguro
4. Salir

ANALISIS 
1. El programa debe verificar si la longitud de una pista disponible es suficiente para el despegue en funcion de la masa del avion

VARIABLES DE ENTRADA
nombre    tipo 
masa      int
l_disp    int 

VARIABLES DE SALIDA 
nombre   tipo 
l_req     int
mensaje   scr

CONSTANTE 
K=15m/ton  int

VARIABLE DE CONTROL 
l_disp >= l_req 

CON 
l_req = k * masa 


'''