primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

print("Os 10 primeiros termos da progressão aritmética são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")
