print("\n", end="")


Valor = int(input("Valor (Reais): "))
print("\n", end="")
Taxa = int(input("Taxa: "))
Tempo = int(input("Tempo: "))

Prestacao = Valor + (Valor * Taxa / 100) * Tempo

print("\n", end="")
print("Prestaçao a pagar: " + str(Prestacao))
print("\n", end="")