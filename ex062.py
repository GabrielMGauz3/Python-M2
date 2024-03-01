primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

termo_atual = primeiro_termo
contador = 0

while True:
    if contador == 10:
        continuar = input("\nDeseja mostrar mais alguns termos? (Digite 0 para encerrar ou qualquer outro número para continuar): ")
        if continuar == '0':
            break
        else:
            quantidade = int(input("Quantos termos deseja mostrar mais? "))
            contador = 0  # Reiniciando o contador
    else:
        print(termo_atual, end=" ")
        termo_atual += razao
        contador += 1