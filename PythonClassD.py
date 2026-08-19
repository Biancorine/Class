print("\n", end="")


Tempo = int(input("Tempo (Horas): "))
print("\n", end="")
Velocidade = int(input("Velocidade(Km/H): "))

Distancia = Tempo * Velocidade
Litros_Usados = Distancia / 12

print("\n", end="")
print("Distância Percorrida: " + str(Distancia))
print("\n", end="")
print("Litros de gasolina usados: " + str(Litros_Usados))
print("\n", end="")