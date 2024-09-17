import os;

opcao = 0;
while opcao != 6:
    os.system('cls')
    print("""Calculadora
          [1] Soma
          [2] Subtração
          [3] Multiplicação
          [4] Divisão
          [5] Exponenciação
          [6] Encerrar o programa
          """);
    
    opcao = int(input("Digite a opção desejada: "));
    
    while opcao == 1:
        os.system('cls');
        print("Soma");
        num1 = int(input("Digite o primeiro número: "));
        num2 = int(input("Digite o segundo número: "));
        print("O resultado da soma é {}".format(num1 + num2));
        
        opcao = input("Deseja realizar outra operação?  Digite 1 para sim e 0 para não");

    
    if opcao == 2:
        os.system('cls');
        print("Subtração");
        num1 = int(input("Digite o primeiro número: "));
        num2 = int(input("Digite o segundo número: "));
        print("O resultado da soma é {}".format(num1 - num2));
        continue