# Ejercicio 1

# Constantes
K = 15      # [m/ton]
a = 0.01    # [1/°C]

def calc_lreq_base(masa):
    resultado = K * masa
    return resultado

def calc_lreq_aj(lreq_base, deltaT):
    resultado = lreq_base * (1 + a * deltaT)
    return resultado

def calc_leff(l_disp, penal):
    resultado = l_disp - penal
    return resultado

def verificar_pista(leff, lreq_aj):
    if leff >= lreq_aj:
        return "La pista es suficiente para el despegue"
    else:
        return "La pista NO es suficiente para el despegue"

#ejercicio 2 


def actualizar_contadores_y_extremos(prev, curr, ascensos, descensos, alt_min, alt_max):
    """Actualiza ascensos, descensos, alt_min y alt_max comparando dos mediciones consecutivas."""
    if curr > prev:
        ascensos += 1
    elif curr < prev:
        descensos += 1

    if curr < alt_min:
        alt_min = curr
    if curr > alt_max:
        alt_max = curr

    return ascensos, descensos, alt_min, alt_max


def suma7(a0, a1, a2, a3, a4, a5, a6):
    return a0 + a1 + a2 + a3 + a4 + a5 + a6


def promedio7(a0, a1, a2, a3, a4, a5, a6):
    return suma7(a0, a1, a2, a3, a4, a5, a6) / 7.0

# Ejercicio 3 
# Constantes
Pmin = 72.0       # [kPa]
Pmax = 82.0       # [kPa]
intervalo = 20    # [min]
dP_lim = 2.0      # [kPa] umbral de variación rápida

def fuera_de_rango(p):
    return (p < Pmin) or (p > Pmax)

def actualizar_extremos(p, p_min, p_max):
    if p < p_min: p_min = p
    if p > p_max: p_max = p
    return p_min, p_max

def actualizar_fuera_y_racha(p, fuera_total_min, racha_act, racha_max):
    if fuera_de_rango(p):
        fuera_total_min += intervalo
        racha_act += 1
        if racha_act > racha_max:
            racha_max = racha_act
    else:
        racha_act = 0
    return fuera_total_min, racha_act, racha_max

def detectar_salto(prev, curr, fugas):
    if abs(curr - prev) > dP_lim:
        fugas += 1
    return fugas

def promedio6(p1, p2, p3, p4, p5, p6):
    return (p1 + p2 + p3 + p4 + p5 + p6) / 6.0

def mensaje_final(fuera_total_min):
    if fuera_total_min > 0:
        return "Activar presurización: se detectaron lecturas fuera de rango."
    return "Presión dentro del rango seguro."

def aviso_fuga(fugas):
    if fugas > 0:
        return f"Atención: variaciones rápidas detectadas ({fugas})."
    return "Sin indicios de variación rápida."
