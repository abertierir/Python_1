def run():
    sentence=input("Ingrese el posible palíndromo: ")
    sentence=str(sentence).replace(" ","").lower
    if sentence==sentence[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

   

if(__name__)=="__main__":
    run()