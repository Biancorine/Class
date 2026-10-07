import os

def calcular_prestacao():
    # Definição das constantes de taxa
    TXMULTA = 0.02  # 2%
    TXJUROS = 0.01  # 1% ao mês

    print("\n--- CÁLCULO DE PRESTAÇÃO EM ATRASO ---")
    
    # Leitura dos dados de entrada
    valor = float(input("Digite o VALOR da prestação (R$): "))
    dias = int(input("Digite a quantidade de DIAS em atraso: "))

    # Processamento (Cálculos conforme fórmulas fornecidas)
    multa = TXMULTA * valor
    juros = TXJUROS * (1 / 30) * dias * valor
    vlpagar = valor + multa + juros

    # Saída dos resultados
    print("\n================ RESUMO ================")
    print(f"Valor Original (VALOR): R$ {valor:.2f}")
    print(f"Dias em Atraso (DIAS): {dias} dia(s)")
    print(f"Valor da Multa (MULTA): R$ {multa:.2f}")
    print(f"Valor dos Juros (JUROS): R$ {juros:.2f}")
    print(f"Valor Total a Pagar (VLPAGAR): R$ {vlpagar:.2f}")
    print("========================================")

def menu():
    while True:
        print("\n" + "="*30)
        print("          MENU PRINCIPAL        ")
        print("="*30)
        print("[ 1 ] Calcular Prestação em Atraso")
        print("[ 2 ] Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            calcular_prestacao()
            input("\nPressione ENTER para continuar...")
        elif opcao == '2':
            print("\nEncerrando o programa... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

# Execução do Programa
if __name__ == "__main__":
    menu()