"""
Este programa calcula a potência de um número dado a base e o expoente.
"""

B = int(input("Digite o valor da base: "))  # Solicita o valor da base ao usuário
E = int(input("Digite o valor do expoente: "))  # Solicita o valor do expoente ao usuário

if B and E < 0:  # Verifica se a base e o expoente são negativos
  print("Entrada inválida")  # Imprime uma mensagem de entrada inválida caso sejam negativos
else:
  print(B**E)  # Calcula e imprime a potência da base elevada ao expoente