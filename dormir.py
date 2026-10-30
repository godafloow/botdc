from random import randint
from datetime import datetime
from zoneinfo import ZoneInfo
import random
import re
import time


# =========================
# CONFIGURACIÓN
# =========================

ZONA_HORARIA = ZoneInfo("Europe/Madrid")

TIEMPO_DESPERTAR = 5 * 60  # 5 minutos

despertar_hasta = 0.0
numero_despertar = random.randint(1, 10)
menciones_despertar = 0


# =========================
# GENERACIÓN DE HORARIOS
# =========================

def random_time(start: int, end: int):
    """
    Devuelve una hora aleatoria entre start y end,
    incluyendo minutos y segundos.
    Formato: HH:MM:SS
    """
    h = randint(start, end)

    if h == 24:
        h = 0

    m = randint(0, 59)
    s = randint(0, 59)

    return f"{h:02d}:{m:02d}:{s:02d}"


def sleeping_hours():
    """
    Genera 7 duraciones de sueño, una por día.
    La suma semanal será de entre 45 y 49 horas.
    """
    while True:
        sleepinghours = [randint(0, 12) for _ in range(7)]
        total = sum(sleepinghours)

        if 44 < total < 50:
            return sleepinghours


def hour_sleep(a: list):
    """
    Genera una hora de inicio de sueño para cada día.
    Devuelve (horas_de_inicio, duraciones).
    """
    horas = []

    for duracion in a:
        if 0 <= duracion < 3:
            hora = random_time(20, 22)
        elif 3 <= duracion < 6:
            hora = random_time(21, 23)
        elif 6 <= duracion < 9:
            hora = random_time(22, 24)
        else:
            hora = random_time(0, 4)

        horas.append(hora)

    return horas, a


HORAS_DORMIR, DURACION_SUENO = hour_sleep(sleeping_hours())


# =========================
# COMPROBAR HORARIO DE SUEÑO
# =========================

def esta_dormida() -> bool:
    """
    Comprueba si el horario semanal indica que el bot debe dormir.
    Tiene en cuenta los periodos que cruzan la medianoche.
    """
    ahora = datetime.now(ZONA_HORARIA)

    dia = ahora.weekday()
    hora_actual = (
        ahora.hour * 3600
        + ahora.minute * 60
        + ahora.second
    )

    # Periodo de sueño que empieza hoy
    hora_texto = HORAS_DORMIR[dia]
    h, m, s = map(int, hora_texto.split(":"))

    inicio_hoy = h * 3600 + m * 60 + s
    duracion_hoy = DURACION_SUENO[dia] * 3600
    fin_hoy = inicio_hoy + duracion_hoy

    dormida_hoy = (
        inicio_hoy <= hora_actual < min(fin_hoy, 24 * 3600)
    )

    # Periodo de sueño que empezó ayer y continúa hoy
    dia_anterior = (dia - 1) % 7

    hora_texto_anterior = HORAS_DORMIR[dia_anterior]
    ha, ma, sa = map(int, hora_texto_anterior.split(":"))

    inicio_ayer = ha * 3600 + ma * 60 + sa
    duracion_ayer = DURACION_SUENO[dia_anterior] * 3600
    fin_ayer = inicio_ayer + duracion_ayer

    dormida_ayer = (
        fin_ayer > 24 * 3600
        and hora_actual < fin_ayer - 24 * 3600
    )

    return dormida_hoy or dormida_ayer


# =========================
# ESTADO DE ACTIVIDAD
# =========================

def esta_despierta() -> bool:
    """
    Está despierta si su horario lo permite
    o si alguien la ha despertado temporalmente.
    """
    if time.monotonic() < despertar_hasta:
        return True

    return not esta_dormida()


# =========================
# DESPERTAR CON NÚMERO
# =========================

async def intentar_despertar(message) -> bool:
    global despertar_hasta, numero_despertar, menciones_despertar

    if message.author.bot or message.guild is None:
        return False

    # Solo cuenta menciones mientras está dormido
    if esta_despierta():
        return False

    # Comprueba si el mensaje menciona al bot
    if message.guild.me not in message.mentions:
        return False

    menciones_despertar += 1

    print(
        f"[DEBUG SUEÑO] Mención {menciones_despertar}/"
        f"{numero_despertar}"
    )

    if menciones_despertar < numero_despertar:
        return False

    menciones_despertar = 0
    despertar_hasta = time.monotonic() + TIEMPO_DESPERTAR

    print(
        f"[DEBUG SUEÑO] ¡Despertado! "
        f"Estará despierto durante {TIEMPO_DESPERTAR // 60} minutos."
    )

    await message.channel.send(
        "¡Me has mencionado suficientes veces! Ya estoy despierto."
    )

    numero_despertar = random.randint(1, 10)

    print(
        f"[DEBUG SUEÑO] Próximo despertar: "
        f"{numero_despertar} menciones."
    )

    return True


# =========================
# INFORMACIÓN DE DEBUG
# =========================

def obtener_estado_debug() -> str:
    ahora = datetime.now(ZONA_HORARIA)

    if time.monotonic() < despertar_hasta:
        segundos = max(
            0,
            int(despertar_hasta - time.monotonic())
        )

        return (
            f"DESPIERTA TEMPORALMENTE | "
            f"Quedan {segundos} segundos"
        )

    return "DORMIDA" if esta_dormida() else "DESPIERTA"


if __name__ == "__main__":
    print("Horario semanal generado:")

    for dia in range(7):
        print(
            f"Día {dia}: "
            f"Inicio {HORAS_DORMIR[dia]} | "
            f"Duración {DURACION_SUENO[dia]} horas"
        )

    print("Número secreto inicial:", numero_despertar)