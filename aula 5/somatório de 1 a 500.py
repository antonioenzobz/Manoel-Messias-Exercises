s = 0  # Variável para armazenar a soma dos números pares
i = 2  # Variável para iterar pelos números pares

while i <= 500:
    s += i  # Adiciona o número par atual à soma
    print(f"A soma de todos os números pares até {i} é: {s}")  # Imprime a soma até o número par atual
    i += 2  # Incrementa para o próximo número par

print("Feito!")  # Indica que o programa terminou