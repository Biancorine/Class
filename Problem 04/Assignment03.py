import sys
import math

valueA = float(input("Digite o valor do lado A: "))

valueB = float(input("Digite o valor do lado B: "))

valueC = float(input("Digite o valor do lado C: "))

if valueA < valueB + valueC and valueB < valueA + valueC and valueC < valueA + valueB:
    print("Os valores digitados podem formar um triângulo.")
    if valueA == valueB and valueB == valueC:
        print("O triângulo é equilátero.")
    elif valueA == valueB or valueA == valueC or valueB == valueC:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os valores digitados não podem formar um triângulo.")