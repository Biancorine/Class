import math

# Inicialização das variáveis e flags booleanas
a = 0.0
b = 0.0
c = 0.0
delta = 0.0
x1 = 0.0
x2 = 0.0
leitura_feita = False
calculo_feito = False

opcao = 0

# Laço principal do programa (continua até a opção ser 4)
while opcao != 4:
    print("\n" + "=" * 20)
    print("        MENU")
    print("=" * 20)
    print("1 - Leitura")
    print("2 - Cálculo")
    print("3 - Impressão")
    print("4 - Saída")
    print("=" * 20)

    opcao = int(input("Escolha uma opção: "))

    # Laço de validação da opção do menu
    while opcao < 1 or opcao > 4:
        print("[!] Opção inválida! Tente novamente.")
        opcao = int(input("Escolha uma opção válida (1 a 4): "))

    if opcao == 1:
        # LEITURA
        a = float(input("\nDigite o coeficiente A (diferente de 0): "))
        
        # Laço de validação do coeficiente A
        while a == 0: 
            print("[!] Erro: O coeficiente A não pode ser zero!")
            a = float(input("Digite o coeficiente A (diferente de 0): "))
        
        b = float(input("Digite o coeficiente B: "))
        c = float(input("Digite o coeficiente C: "))
        
        leitura_feita = True
        calculo_feito = False  # Reseta o cálculo caso o usuário insira novos dados
        print("=> Leitura concluída com sucesso!")

    elif opcao == 2:
        # CÁLCULO
        if not leitura_feita:
            print("\n[!] Erro: Você precisa fazer a Leitura (opção 1) primeiro!")
        else:
            delta = (b ** 2) - (4 * a * c)
            
            if delta >= 0:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                
            calculo_feito = True
            print("\n=> Cálculo realizado com sucesso!")

    elif opcao == 3:
        # IMPRESSÃO
        if not leitura_feita or not calculo_feito:
            print("\n[!] Erro: Você precisa concluir a Leitura (1) e o Cálculo (2) antes de imprimir os resultados!")
        else:
            print("\n--- RESULTADOS ---")
            print(f"Coeficientes: A={a}, B={b}, C={c}")
            print(f"Delta = {delta}")
            
            if delta >= 0:
                print(f"Raiz X1 = {x1}")
                print(f"Raiz X2 = {x2}")
            else:
                print("Sem solução no conjunto dos números Reais!")

    elif opcao == 4:
        # SAÍDA
        print("\nPrograma Finalizado.")