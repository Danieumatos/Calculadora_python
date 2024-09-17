import os

#Função que imprime o menu
def menu():
    limpar_tela()
    print("""Calculadora
          [1] Soma
          [2] Subtração
          [3] Multiplicação
          [4] Divisão
          [5] Exponenciação
          [6] Encerrar o programa
          """);

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Erro! Divisão por 0")

def exponenciacao(num1, num2):
    return num1 ** num2

def limpar_tela():
    os.system('cls')

def calculadora():
    limpar_tela()
    opcao = 0
    while opcao != 6:
        menu()
        
        opcao = int(input("Digite a opção desejada: "))
        
        
        if opcao in [1, 2, 3, 4, 5]:
            limpar_tela()
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        
            if opcao == 1:
                print(f'Resultado: {soma(num1, num2)}')
            elif opcao == 2:
                print(f'Resultado: {subtracao(num1, num2)}')
            elif opcao == 3:
                print(f'Resultado: {multiplicacao(num1, num2)}')
            elif opcao == 4:
                print(f'Resultado: {divisao(num1, num2)}')
            elif opcao == 5:
                print(f'Resultado: {exponenciacao(num1, num2)}')
            input("Pressione enter para continuar...")
        
        elif opcao == 6:
            print("Encerrando o programa...")
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione enter para continuar...")
            
calculadora()