menorv = None  # Variável para armazenar o menor valor
maiorv = None  # Variável para armazenar o maior valor

while True:
  v = int(input("Digite um número maior ou igual a zero: "))  # Solicita ao usuário um número
  if v < 0:  # Se o número for menor que zero, encerra o loop
    break
  if menorv is None or v < menorv:  # Verifica se o número é o menor valor lido até agora
    menorv = v  # Atualiza o menor valor
  if maiorv is None or v > maiorv:  # Verifica se o número é o maior valor lido até agora
    maiorv = v  # Atualiza o maior valor

if menorv is not None:
  print(f"Menor valor lido: {menorv}")  # Imprime o menor valor lido
  print(f"Maior valor lido: {maiorv}")  # Imprime o maior valor lido
else:
  print("Nenhum valor positivo foi lido.")  # Imprime uma mensagem caso nenhum valor positivo tenha sido lido