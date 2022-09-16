def run():
    sentence=input("Ingrese el posible palíndromo: ")
    sentence=str(sentence).replace(" ","")
    sentence_invertida=sentence[::-1].lower
    if sentence==sentence_invertida:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

   

if __name__  == "__main__":
    run()