c = 0  # contador para controlar o número de iterações
n1 = 0  # primeiro número da sequência de Fibonacci
n2 = 1  # segundo número da sequência de Fibonacci

while c <= 10:
  
  f = 1  # variável para armazenar o fatorial de n1
  for i in range(1, n1+1):
    f *= i  # calcula o fatorial de n1
  print(f"O fatorial de {n1} : {f}")  # imprime o fatorial de n1
  
  n1, n2 = n2, n1 + n2  # atualiza os valores de n1 e n2 para a próxima iteração
  c += 1  # incrementa o contador