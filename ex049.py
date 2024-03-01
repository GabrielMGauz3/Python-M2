soma = 0

for numero in range(1, 501, 2):  # começa em 1, termina em 500, passo de 2 para apenas números ímpares
    if numero % 3 == 0:  # verifica se é múltiplo de 3
        soma += numero

print("A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é:", soma)