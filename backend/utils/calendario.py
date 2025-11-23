from datetime import datetime, timedelta

HORA_APERTURA = 10
HORA_CIERRE = 18
DURACION = 2   # estudiantes

def generar_franjas(fecha: datetime.date):
    """
    Genera franjas de 2 horas (para estudiantes).
    """
    franjas = []
    for h in range(HORA_APERTURA, HORA_CIERRE - 1):
        inicio = h
        fin = h + DURACION
        if fin <= HORA_CIERRE:
            franjas.append((inicio, fin))
    return franjas

def formato_hora(h):
    return f"{h:02d}:00"

def dentro_de_7_dias(fecha):
    hoy = datetime.now().date()
    return hoy <= fecha <= hoy + timedelta(days=7)

def es_laborable(fecha):
    # lunes = 0 ... domingo = 6
    return fecha.weekday() in [0, 1, 2, 3, 4]   # L-V

