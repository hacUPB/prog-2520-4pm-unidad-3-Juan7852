'''
1. Evalúa si la pista disponible permite el despegue según masa, temperatura y penalización operativa.
2. Monitoreo de altitud con detección de tendencias y cálculo de parámetros.
3. Control de presiones de cabina con detección de fallas y cálculo de parámetros.
4. Salir
#Se uso AI para los enunciados correctos y algo mas complejos 
ANALISIS 
1. El programa debe verificar si la longitud de una pista disponible es suficiente para el despegue de un avion, considerando la masa, un ajuste por temperatura y una penalizacion operativa que reduce la pista efectiva.

VARIABLES DE ENTRADA
nombre    tipo  
masa      float   en toneladas
l_disp    float   longitud disponible de pista en metros
deltaT    float   exceso de temperatura en °C
penal     float.  penalización operativa en metros

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
k = 15 
a = 0.01
leer 
masa 
l_disp
deltaT
penal

si masa <= 0 o l_disp <=0 o penal <= 0 entonces 
   mostrar "error en parametros"
fin si 

#calculos inteermedios 
lreq_base = K * masa
req_aj = lreq_base * (1 + a * deltaT)
leff = l_disp - penal

si leff >= lreq_aj ENTONCES
        mensaje ← "La pista es suficiente para el despegue"
    sino
        mensaje ← "La pista NO es suficiente para el despegue"
fin si
mostrar "Longitud base requerida: ", lreq_base
mostrar "Longitud ajustada requerida: ", lreq_aj
mostrar "Longitud efectiva disponible: ", leff
mostrar mensaje
fin

2. El sistema debe Registrar siete mediciones de altitud (cada 20 min durante 120 min, incluyendo t=0) y, sin usar estructuras de datos, calcular:
número de ascensos (cuando una medición es mayor que la anterior),
número de descensos (cuando una medición es menor que la anterior),
altitud mínima, máxima y promedio,
y mostrar los resultados al final.


VARIABLES DE ENTRADA

| nombre | tipo  | descripción            |
| ------ | ----- | ---------------------- |
| alt0   | float | altitud en $t=0$ min   |
| alt1   | float | altitud en $t=20$ min  |
| alt2   | float | altitud en $t=40$ min  |
| alt3   | float | altitud en $t=60$ min  |
| alt4   | float | altitud en $t=80$ min  |
| alt5   | float | altitud en $t=100$ min |
| alt6   | float | altitud en $t=120$ min |

VARIABLES DE SALIDA 
| nombre    | tipo  | descripción                                           |
| --------- | ----- | ----------------------------------------------------- |
| ascensos  | int   | cantidad de incrementos entre mediciones consecutivas |
| descensos | int   | cantidad de decrementos entre mediciones consecutivas |
| alt\_min  | float | menor valor entre alt0..alt6                          |
| alt\_max  | float | mayor valor entre alt0..alt6                          |
| alt\_prom | float | promedio de alt0..alt6                                |


CONSTANTE
| nombre    | tipo | valor | descripción                            |
| --------- | ---- | ----- | -------------------------------------- |
| intervalo | int  | 20    | minutos entre mediciones               |
| duracion  | int  | 120   | minutos totales                        |
| n\_meds   | int  | 7     | cantidad de mediciones (incluye t=0) |

VARIABLE DE CONTROL 
Comparaciones entre pares consecutivos
(alt1,alt0),(alt2,alt1),…,(alt6,alt5).

ECUACIONES UTILIZADAS  
Conteo de ascensos/descensos
Para cada par consecutivo:
alt(i)>alt(i-1) ⇒ ascensos = ascensos + 1
alt(i)<alt(i-1) ⇒ descensos = descensos + 1

Mínimo y máximo
Inicializar: alt_min = alt0, alt_max = alt0
Luego, para cada 
alt1..alt6:
si altX < alt_min ⇒ alt_min = altX

Promedio
suma=alt0+alt1+alt2+alt3+alt4+alt5+alt6
alt_prom= suma\n_meds
 
PSUDOCODIGO
INICIO


intervalo = 20
duracion = 120
n_meds ← 7


ascensos = 0
descensos = 0
suma = 0

LEER alt0
LEER alt1
LEER alt2
LEER alt3
LEER alt4
LEER alt5
LEER alt6


alt_min = alt0
alt_max = alt0

SI alt1 > alt0 ENTONCES ascensos = ascensos + 1
SI alt1 < alt0 ENTONCES descensos = descensos + 1
SI alt1 < alt_min ENTONCES alt_min = alt1
SI alt1 > alt_max ENTONCES alt_max = alt1

SI alt2 > alt1 ENTONCES ascensos = ascensos + 1
SI alt2 < alt1 ENTONCES descensos = descensos + 1
SI alt2 < alt_min ENTONCES alt_min = alt2
SI alt2 > alt_max ENTONCES alt_max = alt2

SI alt3 > alt2 ENTONCES ascensos = ascensos + 1
SI alt3 < alt2 ENTONCES descensos = descensos + 1
SI alt3 < alt_min ENTONCES alt_min = alt3
SI alt3 > alt_max ENTONCES alt_max = alt3

SI alt4 > alt3 ENTONCES ascensos = ascensos + 1
SI alt4 < alt3 ENTONCES descensos = descensos + 1
SI alt4 < alt_min ENTONCES alt_min = alt4
SI alt4 > alt_max ENTONCES alt_max = alt4

SI alt5 > alt4 ENTONCES ascensos = ascensos + 1
SI alt5 < alt4 ENTONCES descensos = descensos + 1
SI alt5 < alt_min ENTONCES alt_min = alt5
SI alt5 > alt_max ENTONCES alt_max = alt5

SI alt6 > alt5 ENTONCES ascensos = ascensos + 1
SI alt6 < alt5 ENTONCES descensos = descensos + 1
SI alt6 < alt_min ENTONCES alt_min = alt6
SI alt6 > alt_max ENTONCES alt_max = alt6

suma = alt0 + alt1 + alt2 + alt3 + alt4 + alt5 + alt6
alt_prom = suma / n_meds


MOSTRAR "Ascensos: ", ascensos
MOSTRAR "Descensos: ", descensos
MOSTRAR "Altitud mínima: ", alt_min
MOSTRAR "Altitud máxima: ", alt_max
MOSTRAR "Altitud promedio: ", alt_prom
fin

 
3. El sistema debe rgistrar 6 presiones de cabina (una cada 20 min durante 120 min, sin incluir t=0) y:
verificar en cada medición si está en el rango seguro [72, 82] kPa;
detectar fuga/variación rápida por saltos grandes entre lecturas consecutivas;
calcular mínimo, máximo y promedio;
calcular tiempo total fuera de rango y racha fuera de rango más larga;
emitir un mensaje final (OK / activar presurización) y avisos de variación rápida.


VARIABLES DE ENTRADA
| nombre                 | tipo  | descripción                                  |
| ---------------------- | ----- | -------------------------------------------- |
| p1, p2, p3, p4, p5, p6 | float | presiones en kPa en cada tiempo (20→120 min) |


VARIABLES DE SALIDA 
| nombre                  | tipo  | descripción                                         |
| ----------------------- | ----- | --------------------------------------------------- |
| p\_min, p\_max, p\_prom | float | mínimo, máximo y promedio de las 6 lecturas         |
| fuera\_total\_min       | int   | minutos acumulados fuera de rango                   |
| racha\_max              | int   | mayor número consecutivo de lecturas fuera de rango |
| fugas                   | int   | conteo de “saltos” grandes entre mediciones         |
| mensaje                 | str   | “OK” o “Activar presurización”                      |
| aviso\_fuga             | str   | mensaje si se detectan variaciones rápidas          |


CONSTANTE 
| nombre    | valor   | descripción                                                 |
| --------- | ------- | ----------------------------------------------------------- |
| Pmin      | 72 kPa  | límite inferior seguro                                      |
| Pmax      | 82 kPa  | límite superior seguro                                      |
| intervalo | 20 min  | separación entre mediciones                                 |
| ΔP\_lim   | 2.0 kPa | umbral de **variación rápida** entre mediciones (ajustable) |

VARIABLES DE CONTROL 
Comparar cada presión con límites y con la anterior: pares (p2,p1), (p3,p2), …, (p6,p5).

ECUACIOENES / REGLAS
Fuera de rango por medición
fuera(pX) = (pX < Pmin) OR (pX > Pmax)

Tiempo fuera de rango
fuera_total_min = (#lecturas_fuera) * intervalo

Racha fuera de rango
recorrer p1..p6; si fuera(pX) aumenta racha_actual, si no, reinicia; mantener racha_max.
Mín, máx, promedio
p_min = min(p1..p6); p_max = max(p1..p6); p_prom = (p1+p2+...+p6)/6

Variación rápida (posible fuga)
para cada salto: ΔP = |pX - p(X-1)|; si ΔP > ΔP_lim ⇒ fugas += 1

Mensaje final
Si alguna medición está fuera de [Pmin, Pmax] ⇒ “Activar presurización”
Si todas dentro ⇒ “Presión dentro del rango seguro”
(y agregar aviso si fugas > 0)

PSEUDOCIDIGO
INICIO

Pmin = 72.0
Pmax = 82.0
intervalo = 20
ΔP_lim = 2.0

LEER p1 p2 p3 p4 p5 p6


fuera_total_min = 0
racha_actual = 0
racha_max = 0
fugas = 0


p_min = p1
p_max = p1
suma = p1

    SI (p1 < Pmin) O (p1 > Pmax) ENTONCES
        fuera_total_min = fuera_total_min + intervalo
        racha_actual = racha_actual + 1
        SI racha_actual > racha_max ENTONCES racha_max = racha_actual 
    SINO
        racha_actual = 0
    FIN SI

    // ---- p2 ----
    suma = suma + p2
    SI p2 < p_min ENTONCES p_min = p2 FIN SI
    SI p2 > p_max ENTONCES p_max = p2 FIN SI

    SI (p2 < Pmin) O (p2 > Pmax) ENTONCES
        fuera_total_min = fuera_total_min + intervalo
        racha_actual = racha_actual + 1
        SI racha_actual > racha_max ENTONCES racha_max = racha_actual FIN SI
    SINO
        racha_actual ← 0
    FIN SI

    SI ABS(p2 - p1) > ΔP_lim ENTONCES fugas = fugas + 1 FIN SI
    *("Si la variación en magnitud entre p2 y p1 es mayor que el límite permitido, contarla como una posible fuga".)*

    // ---- p3 ----
    suma ← suma + p3
    SI p3 < p_min ENTONCES p_min ← p3 FIN SI
    SI p3 > p_max ENTONCES p_max ← p3 FIN SI

    SI (p3 < Pmin) O (p3 > Pmax) ENTONCES
        fuera_total_min ← fuera_total_min + intervalo
        racha_actual ← racha_actual + 1
        SI racha_actual > racha_max ENTONCES racha_max ← racha_actual FIN SI
    SINO
        racha_actual ← 0
    FIN SI

    SI ABS(p3 - p2) > ΔP_lim ENTONCES fugas ← fugas + 1 FIN SI

    // ---- p4 ----
    suma ← suma + p4
    SI p4 < p_min ENTONCES p_min ← p4 FIN SI
    SI p4 > p_max ENTONCES p_max ← p4 FIN SI

    SI (p4 < Pmin) O (p4 > Pmax) ENTONCES
        fuera_total_min ← fuera_total_min + intervalo
        racha_actual ← racha_actual + 1
        SI racha_actual > racha_max ENTONCES racha_max ← racha_actual FIN SI
    SINO
        racha_actual ← 0
    FIN SI

    SI ABS(p4 - p3) > ΔP_lim ENTONCES fugas ← fugas + 1 FIN SI

    // ---- p5 ----
    suma ← suma + p5
    SI p5 < p_min ENTONCES p_min ← p5 FIN SI
    SI p5 > p_max ENTONCES p_max ← p5 FIN SI

    SI (p5 < Pmin) O (p5 > Pmax) ENTONCES
        fuera_total_min ← fuera_total_min + intervalo
        racha_actual ← racha_actual + 1
        SI racha_actual > racha_max ENTONCES racha_max ← racha_actual FIN SI
    SINO
        racha_actual ← 0
    FIN SI

    SI ABS(p5 - p4) > ΔP_lim ENTONCES fugas ← fugas + 1 FIN SI

    // ---- p6 ----
    suma ← suma + p6
    SI p6 < p_min ENTONCES p_min ← p6 FIN SI
    SI p6 > p_max ENTONCES p_max ← p6 FIN SI

    SI (p6 < Pmin) O (p6 > Pmax) ENTONCES
        fuera_total_min ← fuera_total_min + intervalo
        racha_actual ← racha_actual + 1
        SI racha_actual > racha_max ENTONCES racha_max ← racha_actual FIN SI
    SINO
        racha_actual ← 0
    FIN SI

    SI ABS(p6 - p5) > ΔP_lim ENTONCES fugas ← fugas + 1 FIN SI

    // --- Promedio ---
    p_prom ← suma / 6

    // --- Mensajes ---
    SI fuera_total_min > 0 ENTONCES
        mensaje ← "Activar presurización: se detectaron lecturas fuera de rango."
    SINO
        mensaje ← "Presión dentro del rango seguro."
    FIN SI

    SI fugas > 0 ENTONCES
        aviso_fuga ← "Atención: variaciones rápidas detectadas (" + fugas + ")."
    SINO
        aviso_fuga ← "Sin indicios de variación rápida."
    FIN SI

    // --- Salidas ---
    MOSTRAR "p_min (kPa): ", p_min
    MOSTRAR "p_max (kPa): ", p_max
    MOSTRAR "p_prom (kPa): ", p_prom
    MOSTRAR "Tiempo fuera de rango (min): ", fuera_total_min
    MOSTRAR "Racha fuera de rango más larga (lecturas): ", racha_max
    MOSTRAR aviso_fuga
    MOSTRAR mensaje

FIN

'''
