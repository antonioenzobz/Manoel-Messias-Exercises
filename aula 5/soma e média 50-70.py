n = 50  # Inicializa o contador com o valor 50
s = 0  # Inicializa a variável de soma com o valor 0
c = 0  # Inicializa o contador de números pares com o valor 0

while n <= 70:  # Enquanto o contador for menor ou igual a 70
  if n % 2 == 0:  # Se o número atual for par
    s = s + n  # Adiciona o número atual à soma
    c = c + 1  # Incrementa o contador de números pares
  n = n + 1  # Incrementa o contador

print(f"A soma de todos os pares de 50 a 70 é igual a {s} e a média é igual a {s/c}")  # Imprime a soma e a média dos números pares