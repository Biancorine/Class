import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

Delta = B**2 - 4*A*C

if Delta > 0:
    Raiz1 = (-B + math.sqrt(Delta)) / (2*A)
    Raiz2 = (-B - math.sqrt(Delta)) / (2*A)

    print(f"X1 = {Raiz1}")
    print(f"X2 = {Raiz2}")

elif Delta == 0:
    Raiz1 = -B / (2*A)

    print(f"X1 e X2 = {Raiz1}")

else:
    print("Essa equação não possui raízes")