n = 0  # contador para armazenar o total de valores lidos
s = 0  # variável para armazenar o somatório dos valores

while True:
  v = float(input("Digite um valor maior ou igual a zero: "))  # solicita ao usuário um valor
  if v < 0:  # verifica se o valor é negativo
    break  # encerra o loop caso seja negativo
  n += 1  # incrementa o contador de valores lidos
  s += v  # adiciona o valor ao somatório

if n != 0:
  média = s / n  # calcula a média dos valores lidos
  print(f"Total de valores lidos: {n}")  # exibe o total de valores lidos
  print(f"Soma dos valores lidos {s}")  # exibe o somatório dos valores lidos
  print(f"Média dos valores lidos: {média}")  # exibe a média dos valores lidos
else:
  print("Nenhum número positivo foi lido.")  # exibe uma mensagem caso nenhum número positivo tenha sido lido