from datetime import datetime

anio_actual = datetime.now().year

anio_pasado = int(input("Ingresa un año pasado (por ejemplo, 1950): "))

fecha_actual = datetime(anio_actual, 1, 1)
fecha_pasada = datetime(anio_pasado, 1, 1)

diferencia_anios = fecha_actual.year - fecha_pasada.year

print(f"Hay {diferencia_anios} años de diferencia hacia el pasado ({fecha_pasada.year}).")

anio_futuro = int(input("Ingresa un año futuro (por ejemplo, 2050): "))

fecha_futura = datetime(anio_futuro, 1, 1)

anios_hasta_futuro = fecha_futura.year - anio_actual

print(f"Faltan {anios_hasta_futuro} años para llegar al año {fecha_futura.year}.")
