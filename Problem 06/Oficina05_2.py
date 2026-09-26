import math

# Inicialização das variáveis, tal como no bloco verde do diagrama
a = 0.0
b = 0.0
c = 0.0
triangulo = False

while True:
    # Menu (Bloco laranja: Entrada/Saída)
    tecla = int(input("\n1 Ler e Exibir\n2 Sair\nitem: "))

    # "Caso 1" no diagrama (Losango azul)
    if tecla == 1:
        # Bloco laranja: Entrada de dados A, B, C
        a = float(input("\nDigite o lado A: "))
        b = float(input("Digite o lado B: "))
        c = float(input("Digite o lado C: "))

        # Losango azul: Condição de existência do triângulo
        if (a < b + c) and (b < a + c) and (c < a + b):
            # Bloco verde (SIM)
            triangulo = True
        else:
            # Bloco verde (NÃO)
            triangulo = False

        # Losango azul: Testa a flag 'triangulo'
        if triangulo == True:
            # Bloco laranja (SIM)
            print("Trata-se de um Triângulo!")
            
            # --- Início dos cálculos solicitados na Oficina 5 ---
            # Cálculo do Semiperímetro (S)
            s = (a + b + c) / 2
            
            # Cálculo da Área usando a Fórmula de Heron
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            
            print(f"Semiperímetro (S): {s}")
            print(f"Área: {area:.2f}")
            # --- Fim dos cálculos ---

        else:
            # Bloco laranja (NÃO)
            print("Uma figura qualquer de três lados")

    # "Caso 2" no diagrama (Losango azul)
    elif tecla == 2:
        # Bloco verde: FINALIZAR PROGRAMA
        print("\nFINALIZAR PROGRAMA")
        break # Interrompe o loop 'while True', indo para o "FINAL"

    # Tratamento para opções inválidas (não explícito no diagrama, mas boa prática)
    else:
        print("\n[!] Opção inválida! Tente novamente.")