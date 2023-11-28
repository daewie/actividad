num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

if num1 == num2 == num3 == num4:
    print("Todos los números son iguales.")
elif num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    print("Hay al menos un número repetido al menos dos veces.")
else:
    print("Todos los números son diferentes.")