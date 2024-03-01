def eh_palindromo(frase):
    # Removendo os espaços da frase e convertendo para minúsculas
    frase_formatada = frase.replace(" ", "").lower()
    # Verificando se a frase é igual à sua versão invertida
    return frase_formatada == frase_formatada[::-1]

frase = input("Digite uma frase: ")

if eh_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")