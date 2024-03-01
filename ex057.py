# Coletando variáveis
soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0

# Coletando dados sobre as 4 pessoas
for i in range(1, 5):
    print(f"---- Pessoa {i} ----")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    # Somando as idades para calcular a média depois
    soma_idades += idade

    # Verificando se é homem e se é o mais velho até agora
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Verificando se é mulher e se tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calculando a média de idade
media_idade = soma_idades / 4

# Exibindo os resultados
print("\n--- Resultados ---")
print("A média de idade do grupo é:", media_idade)
print("O homem mais velho é:", nome_homem_mais_velho)
print("Quantidade de mulheres com menos de 20 anos:", mulheres_menos_20)