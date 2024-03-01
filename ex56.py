# Coletando variáveis para armazenar o maior e o menor peso
maior_peso = float('-inf')  # Inicializa com o menor valor possível
menor_peso = float('inf')   # Inicializa com o maior valor possível

# Interando sobre as 5 pessoas
for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))

    # Atualizando o maior e o menor peso, se necessário
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

# Exibindo o maior e o menor peso
print("\nO maior peso entre as 5 pessoas é:", maior_peso)
print("O menor peso entre as 5 pessoas é:", menor_peso)