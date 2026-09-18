import sys
import math

lados = int(input("Quantos lados tem o poligono?: "))

while lados < 3 or lados > 5:
    if lados < 3:
        print("Não é um poligo, insira outro valor")
        lados = int(input("Quantos lados tem o poligono?: "))
    elif lados > 5:
        print("Poligono não identificado, insira outro valor")
        lados = int(input("Quantos lados tem o poligono?: "))

if lados == 3:

    print("O poligono é um triangulo")
    lado1 = float(input("Digite o valor do lado 1 cm: "))
    lado2 = float(input("Digite o valor do lado 2 cm: "))
    lado3 = float(input("Digite o valor do lado 3 cm: "))

    p = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(p * (p - lado1) * (p - lado2) * (p - lado3))
    printf("A area do triangulo é: {area}cm²")
    sys.exit()
    # Esse código calcula a área de um triângulo usando a fórmula de Heron, deve funcionar com qualquer triângulo.

if lados == 4:
    
    print("O poligono é um quadrado")
    lado = float(input("Digite o valor do lado cm: "))
    area = lado * lado
    printf("A area do quadrado é: {area}cm²")
    sys.exit()
    # Esse código calcula a área de um quadrado, que é simplesmente o lado ao quadrado.

if lados == 5:
    
    print("O poligono é um pentagono")
    lado = float(input("Digite o valor do lado cm: "))
    area = (5 * lado * lado) / (4 * math.tan(math.pi / 5))
    printf("A area do pentagono é: {area}cm²")
    sys.exit()
    # Esse código calcula a área de um pentágono regular usando a fórmula: (5 * lado^2) / (4 * tan(π/5)), funciona apenas com pentágonos regulares.