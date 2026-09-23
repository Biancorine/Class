import math

# Entrada dos lados do triângulo
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

# Cálculo do semiperímetro
s = (a + b + c) / 2

# Cálculo da área utilizando a Fórmula de Heron
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Exibição dos resultados
print(f"Semiperímetro (S): {s}")
print(f"Área do Triângulo: {area:.2f}")