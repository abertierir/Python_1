def run():
    sentence=input("Ingrese el posible palíndromo: ")
    sentence=str(sentence).replace(" ","")
    sentence=sentence.lower
    print("la sentence es: "+sentence )
    sentence_invertida=sentence[::-1]
    if sentence==sentence_invertida:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

   

if __name__  == "__main__":
    run()