def convertir_moneda (tipo_moneda, valor_dolar):
    pesos = input("¿Cuantos pesos "+tipo_moneda+" tienes? ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares=round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de moneda 🌈

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""

opcion=int(input(menu))

if opcion==1:
    convertir_moneda("colombianos",4500)
elif opcion==2:
    convertir_moneda("colombianos",140.60)
elif opcion==3:
    convertir_moneda("mexicanos",20.16)
else:
    print("Inserte una opción válida sopendejo")


# dolares = input("¿Cuantos dólares tienes? ")
# dolares = float(dolares)
# pesos = dolares*valor_dolar
# pesos = round(pesos,2)
# pesos = str(pesos)
# print("Tienes $"+pesos+" pesos COP")

