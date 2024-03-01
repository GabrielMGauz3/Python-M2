from datetime import date

# Obtendo o ano atual
ano_atual = date.today().year

# Inicializando contadores
menores_idade = 0
maiores_idade = 0

# Iterando sobre as 7 pessoas
for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        menores_idade += 1
    else:
        maiores_idade += 1

print(f"\nDas 7 pessoas:")
print(f"{menores_idade} ainda não atingiram a maioridade.")
print(f"{maiores_idade} já são maiores de idade.")