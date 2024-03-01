#JOGO DO PAR OU IMPAR

import random

vitorias_consecutivas = 0

while True:
    jogador = input("Par ou Ímpar? (P/I): ").upper()
    if jogador not in ['P', 'I']:
        print("Escolha inválida. Tente novamente.")
        continue

    jogador_numero = int(input("Digite um número entre 1 e 10: "))
    computador_numero = random.randint(1, 10)

    soma = jogador_numero + computador_numero
    resultado = "Par" if soma % 2 == 0 else "Ímpar"

    print(f"Você escolheu {jogador_numero} e o computador escolheu {computador_numero}.")
    print(f"A soma dos números é {soma}, que é {resultado}.")

    if (resultado == "Par" and jogador == "P") or (resultado == "Ímpar" and jogador == "I"):
        print("Você ganhou!")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu!")
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")