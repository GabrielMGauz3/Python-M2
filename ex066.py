#TABUADO V3
while True:
    numero = int(input("Digite um número para ver sua tabuada (ou um número negativo para sair): "))

    if numero < 0:
        print("Programa encerrado.")
        break

    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")