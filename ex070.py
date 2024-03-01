while True:
    valor_saque = int(input("Digite o valor que deseja sacar: "))

    cedulas_disponiveis = [50, 20, 10, 1]
    quantidade_cedulas = [0, 0, 0, 0]

    for i in range(len(cedulas_disponiveis)):
        while valor_saque >= cedulas_disponiveis[i]:
            quantidade_cedulas[i] += 1
            valor_saque -= cedulas_disponiveis[i]

    print("\nCédulas entregues:")
    for i in range(len(cedulas_disponiveis)):
        if quantidade_cedulas[i] > 0:
            print(f"{quantidade_cedulas[i]} cédula(s) de {cedulas_disponiveis[i]}")

    continuar = input("\nDeseja fazer um novo saque? (S/N): ").upper()
    if continuar != 'S':
        print("Obrigado por usar nosso caixa eletrônico. Até mais!")
        break