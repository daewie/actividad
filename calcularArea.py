# AREA DE CUADRADO

lado = float(input("ingrese el area lado del cuadrado: "))
area_cuadrado = lado ** 2
print(f"el area del cuadrado es: {area_cuadrado}")

# AREA DEL TRIANGULO

altura = float(input("ingrese la altura del triangulo: "))
base = float(input("Ingrese la base del triangulo: "))
area_triangulo = 0.5 * altura * base

print(f"El area del triangulo es de: {area_triangulo}")

# AREA DEL CIRCULO 

import math
radio = float(input("ingrese el radio del circulo: "))
area_circulo = math.pi * radio ** 2

print(f"El area del circulo es de {area_circulo}")

# AREA DE RECTANGULO

base_rectangulo = float(input("Ingrese la base del rectangulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectangulo: "))
area_rectangulo = base_rectangulo * altura_rectangulo

print(f"El area de rectangulo es de: {area_rectangulo}")