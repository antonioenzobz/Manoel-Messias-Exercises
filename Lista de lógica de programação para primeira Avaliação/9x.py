lista = []  # Cria uma lista vazia
for i in range(5):  # Loop para solicitar 5 números ao usuário
  lista.append(int(input(f"Digite o {i + 1}º número: ")))  # Adiciona o número digitado à lista
valor = int(input("Digite o valor a ser pesquisado: "))  # Solicita o valor a ser pesquisado
inicio = 0  # Define o índice inicial da busca
fim = len(lista) - 1  # Define o índice final da busca
while inicio <= fim:  # Loop para realizar a busca binária
  posi = (inicio + fim) // 2  # Calcula o índice do elemento do meio
  if lista[posi] == valor:  # Verifica se o valor foi encontrado
    print(f"O valor {valor} ocorre na posição {posi}")  # Imprime a posição do valor encontrado
    break  # Encerra o loop
  elif lista[posi] < valor:  # Verifica se o valor está na metade superior da lista
    inicio = posi + 1  # Atualiza o índice inicial da busca
  else:  # O valor está na metade inferior da lista
    fim = posi - 1  # Atualiza o índice final da busca
else:  # Executado quando o loop while termina sem encontrar o valor
  print("O valor não ocorre na lista")  # Imprime uma mensagem informando que o valor não foi encontrado