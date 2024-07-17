p = input("Digite uma palavra: ")  # Solicita ao usuário que digite uma palavra

if p == p[::-1]:  # Verifica se a palavra é igual à sua versão invertida
  print(f"A palavra {p} é um palíndromo!")  # Imprime uma mensagem informando que a palavra é um palíndromo
else:
  print(f"A palavra {p} não é um palíndromo!")  # Imprime uma mensagem informando que a palavra não é um palíndromo