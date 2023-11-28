menu_colores =["amarillo","azul","rojo","blanco","negro"]
print("COLORES DISPONIBLES:   ")
for i,color in enumerate(menu_colores, 1):
    print(f"{i},{color}")
opcion1 = int(input("seleccione el primer color (seleccione el numero)"))
opcion2 = int(input("seleccione el segundo numero (seleccione un numero)"))
if 1 <= opcion1 <= len(menu_colores) and 1 <= opcion2 <= len(menu_colores):
    color1 = menu_colores[opcion1 - 1]
    color2 = menu_colores[opcion2 - 1]
    if (color1 == "amarillo" and color2 == "azul" ) or (color1 == "azul" and color2 == "amarillo"):
        print("la combinacion da amarillo")
    elif(color1 == "amarillo" and color2 == "rojo") or (color1 == "rojo" and color2 == "amarillo"):
        print("la combinacion genera naranja")
    elif (color1 == "azul" and color2 == "rojo") or (color1 == "rojo" and color2 == "azul"):
        print("la combinación genera morado.")
    elif (color1 == "blanco" or color2 == "blanco"):
        print("la combinación con blanco no cambia el color.")
    elif (color1 == "negro" or color2 == "negro"):
        print("la combinación con negro oscurece el color.")
    else:
            print("No existe combinación posible con los colores seleccionados.")
else:
        print("Opción no válida. Por favor, seleccione un número válido del menú.")


