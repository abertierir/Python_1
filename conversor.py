menu = """
Bienvenido al conversor de moneda 🌈

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""

opcion=int(input(menu))

if opcion==1:
    pesos = input("¿Cuantos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 4500
    dolares = pesos/valor_dolar
    dolares=round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion==2:
    pesos = input("¿Cuantos pesos argentinos tienes? ")
    pesos = float(pesos)
    valor_dolar = 140.60
    dolares = pesos/valor_dolar
    dolares=round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion==3:
    pesos = input("¿Cuantos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 20.16
    dolares = pesos/valor_dolar
    dolares=round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Inserte una opción válida sopendejo")


dolares = input("¿Cuantos dólares tienes? ")
dolares = float(dolares)
pesos = dolares*valor_dolar
pesos = round(pesos,2)
pesos = str(pesos)
print("Tienes $"+pesos+" pesos COP")

