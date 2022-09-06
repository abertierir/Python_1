pesos = input("¿Cuantos pesos colombianos tienes? ")
pesos = float(pesos)
valor_dolar = 4500
dolares = pesos/valor_dolar
dolares=round(dolares,2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
dolares = input("¿Cuantos dólares tienes? ")
dolares = float(dolares)
pesos = dolares*valor_dolar
pesos = round(pesos,2)
pesos = str(pesos)
print("Tienes $"+pesos+" pesos COP")