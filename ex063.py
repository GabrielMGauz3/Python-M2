n = int(input("Digite o número de elementos da sequência Fibonacci que você deseja exibir: "))

# Inicializando os dois primeiros termos da sequência Fibonacci
fibonacci = [0, 1]

# Calculando os próximos termos da sequência Fibonacci
for i in range(2, n):
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_termo)

# Exibindo os n primeiros termos da sequência Fibonacci
print("Os", n, "primeiros termos da sequência Fibonacci são:")
for termo in fibonacci:
    print(termo, end=" ")