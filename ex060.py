while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\nMenu:")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("4 - Novos números")
    print("5 - Sair do programa")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Resultado da soma:", (num1 + num2))
    elif opcao == 2:
        print("Resultado da multiplicação:", (num1 * num2))
    elif opcao == 3:
        print("Resultado divisão", (num1 / num2))
    elif opcao == 4:
        continue
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")