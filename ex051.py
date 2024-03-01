soma = 0

for c in range(6):  # Loop para ler seis números
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero  # Adiciona o número par à soma

print("A soma dos números pares é:", soma)