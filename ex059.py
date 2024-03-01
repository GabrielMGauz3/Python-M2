import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 10)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("O computador pensou em um número de 0 a 10. Tente adivinhar.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print("Parabéns, você acertou!")
            print("Número de tentativas:", tentativas)
            break
        elif palpite < numero_secreto:
            print("O número é maior. Tente novamente.")
        else:
            print("O número é menor. Tente novamente.")

jogo_adivinhacao()