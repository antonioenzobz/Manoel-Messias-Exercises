lista = []

# Preenche a lista com 15 números fornecidos pelo usuário
for i in range(1, 16):
  n = int(input(f"Digite o número {i} da lista: "))
  lista.append(n)

x = int(input("Digite um número inteiro a ser procurado na lista: "))

# Conta quantas vezes o número x aparece na lista
contador = lista.count(x)
print(f"O número {x} aparece {contador} vezes na lista.")
