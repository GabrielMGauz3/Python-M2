while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print("Valor incorreto. Por favor, digite M para masculino ou F para feminino.")

print("Sexo registrado:", sexo)