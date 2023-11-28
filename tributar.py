edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))

if edad >= 18 and ingresos_mensuales >= 2500000:
    print("Usted debe tributar.")
else:
    print("Usted no tiene que tributar.")