'''
1. Verificar si la longitud de pista disponible es suficiente para el despegue del avión.
2. Registrar la altitud de vuelo cada 20 minutos durante dos horas y mostrar todas las mediciones al final.
3. ⁠Registrar la presión de cabina cada 20 minutos durante 2 hora y comprobar en cada medición si se mantiene dentro del rango seguro
4. Salir

ANALISIS 
1. El programa debe verificar si la longitud de una pista disponible es suficiente para el despegue de un avion, considerando la masa, un ajuste por temperatura y una penalizacion operativa que reduce la pista efectiva.

VARIABLES DE ENTRADA
nombre    tipo 
masa      float
l_disp    float 
deltaT    float
penal     float

VARIABLES DE SALIDA 
nombre   tipo 
lreq_base  float
lreq_aj    float 
leff       float 
mensaje   str

CONSTANTE 
K=15m/ton  int   factor base de masa pista
a=0.01°C   float   aumento relativo por °C de exceso (1% por °C)

VARIABLE DE CONTROL 
leff >= l_req_aj

ECUACIONES UTILIZADAS  
lreq_base = K * masa
leff = ldisp - penal
lreg_ab = lreq_base x (1 + a + delT)

PSUDOCODIGO
leer 
masa 
l_disp
deltaT
penal
si masa <= 0 o l_disp <=0 o penal <= 0 entonces 
   mostrar "error en parametros"
fin si 

k = 15 
a = 0.01


aun hay que modificar 2 y 3*** 
2. El sistema debe almacenar una serie de altitud tomada a intervalos fijos y mostrar todas las mediciones al finalizar el periodo

VARIABLES DE ENTRADA
nombre  tipo 
alt     float

VARIABLES DE SALIDA 
nombre   tipo 
altitudes float
tiempos   int
n_meds    int 

CONSTANTE
intervalo = 20 
duracion = 120 

VARIABLE DE CONTROL 

ECUACIONES UTILIZADAS  
n_meds = durancion/intervalo + 1 con t=0
 
3. El sistema registra la presión de cabina cada 20 minutos durante 2 horas (6 mediciones). En cada registro se verifica si la presión está dentro del rango seguro (72–82 kPa). Si en algún momento está fuera de rango, se indica que debe activarse el sistema de presurización

VARIABLES DE ENTRADA
nombre    tipo 
presion    float

VARIABLES DE SALIDA 
nombre   tipo 
presiones float
tiempo    int 
mensaje   str

CONSTANTE 
Pmin = 72kpa
Pmax = 82kpa

'''