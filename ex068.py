pessoas_mais_18 = 0
homens_cadastrados = 0
mulheres_mais_20 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()

    if idade > 18:
        pessoas_mais_18 += 1

    if sexo == 'M':
        homens_cadastrados += 1
    elif sexo == 'F' and idade > 20:
        mulheres_mais_20 += 1

    continuar = input("Deseja cadastrar mais uma pessoa? (S/N): ").upper()
    if continuar != 'S':
        break

print("a) Quantidade de pessoas com mais de 18 anos:", pessoas_mais_18)
print("b) Quantidade de homens cadastrados:", homens_cadastrados)
print("c) Quantidade de mulheres com mais de 20 anos cadastradas:", mulheres_mais_20)