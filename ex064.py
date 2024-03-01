soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (ou 999 para parar): "))

    if numero == 999:
        break

    soma += numero
    contador += 1

print("Foram digitados", contador, "números.")
print("A soma dos números digitados é:", soma)
