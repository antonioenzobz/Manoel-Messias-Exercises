n = 1  # Inicializa o contador n com o valor 1
sf = 0  # Inicializa a variável sf (somatório dos fatoriais) com o valor 0

while n <= 10:  # Executa o loop enquanto n for menor ou igual a 10
  if n % 2 != 0:  # Verifica se n é ímpar
    f = 1  # Inicializa a variável f (fatorial) com o valor 1
    for i in range(1, n + 1):  # Executa o loop para calcular o fatorial de n
      f *= i  # Multiplica f por cada número no intervalo de 1 a n
    print(f"O fatorial de {n} é: {f}")  # Imprime o resultado do fatorial de n
  sf = sf + f  # Adiciona o fatorial de n ao somatório sf
  n += 1  # Incrementa o contador n

print(f"O somatório de todos os ímpares de 1 a 10 é igual a {sf}")  # Imprime o somatório sf dos fatoriais dos números ímpares de 1 a 10