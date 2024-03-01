soma = 0
contador = 0
maior = menor = 0
while True:
    numero = int(input("Digite um número inteiro: "))

    soma += numero
    contador += 1

    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != 'S':
        break

if contador == 0:
    print("Nenhum número foi digitado.")
else:
    media = soma / contador
    print("Média dos números:", media)
    print("Maior número digitado:", maior)
    print("Menor número digitado:", menor)