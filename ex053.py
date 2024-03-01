def verificar_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Se for divisível por algum número além de 1 e ele mesmo, não é primo
    return True

numero = int(input("Digite um número inteiro: "))

if verificar_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")