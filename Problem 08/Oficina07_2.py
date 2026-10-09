# -*- coding: utf-8 -*-

# --- SUB-ROTINA DE LEITURA (Função) ---
def ler_comprimento():
    return float(input("Digite o comprimento do círculo: "))

# --- SUB-ROTINAS DE CÁLCULO (Funções) ---
def getDiametro(comprimento):
    return comprimento / 3.14

def getRaio(diametro):
    return diametro / 2

def getArea(raio):
    return raio * raio * 3.14

# --- SUB-ROTINA DE SAÍDA (Processo) ---
def exibir_resultados(diametro, raio, area):
    print("\n--- RESULTADOS ---")
    print(f"Diâmetro calculado: {diametro:.2f}")
    print(f"Raio calculado: {raio:.2f}")
    print(f"Área calculada: {area:.2f}")
    print("------------------")

# --- MENU INFINITO DE CONTROLO (Processo) ---
def menu_circulo():
    comprimento = 0.0
    diametro = 0.0
    raio = 0.0
    area = 0.0
    
    while True:
        print("\n==============================")
        print("      MENU DO CÍRCULO         ")
        print("==============================")
        print("1 - Ler Comprimento")
        print("2 - Calcular Diâmetro, Raio e Área")
        print("3 - Exibir Resultados")
        print("4 - Sair do Programa")
        print("==============================")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            comprimento = ler_comprimento()
            print("✓ Comprimento registado!")
            
        elif opcao == "2":
            if comprimento > 0:
                diametro = getDiametro(comprimento)
                raio = getRaio(diametro)
                area = getArea(raio)
                print("✓ Cálculos realizados!")
            else:
                print("Erro: Leia o comprimento (Opção 1) primeiro.")
                
        elif opcao == "3":
            if diametro > 0:
                exibir_resultados(diametro, raio, area)
            else:
                print("Erro: Faça os cálculos (Opção 2) primeiro.")
                
        elif opcao == "4":
            print("A encerrar o programa...")
            break
            
        else:
            print("Opção inválida!")

menu_circulo()