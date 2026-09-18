import sys

lados = int(input("Quantos lados tem o poligono?: "))

while lados < 3 or lados > 5:
    if lados < 3:
        print("Não é um poligo, insira outro valor")
        lados = int(input("Quantos lados tem o poligono?: "))
    elif lados > 5:
        print("Poligono não identificado, insira outro valor")
        lados = int(input("Quantos lados tem o poligono?: "))