def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    print("O fatorial de", numero, "é:", calcular_fatorial(numero))