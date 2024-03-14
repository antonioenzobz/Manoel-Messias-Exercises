# Inicializando as variáveis
n = 0  # contador
a = 0  # primeiro número da sequência
b = 1  # segundo número da sequência

# Loop para imprimir a sequência de Fibonacci
while n <= 15: # contador
    print(a)  # imprime o número atual da sequência
    a, b = b, a + b  # atualiza os valores de a e b para o próximo número da sequência
    n += 1  # incrementa o contador