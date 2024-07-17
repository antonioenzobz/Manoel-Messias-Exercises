lista = []

# Preenche a lista com 20 números fornecidos pelo usuário
for i in range(1, 21):
  n = int(input(f"Digite o número {i} da lista: "))
  lista.append(n)
  
# Calcula a moda (valor mais frequente na lista)
moda = max(set(lista), key=lista.count)

# Ordena a lista em ordem crescente
lista.sort()

# Calcula a mediana (valor do meio da lista)
if len(lista) % 2 == 0:
    mediana = (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2
else:
    mediana = lista[len(lista) // 2]

# Calcula a média dos valores da lista
media = sum(lista) / 20

# Imprime os resultados
print(f"A moda é de: {moda}")
print(f"A mediana é de: {mediana}")
print(f"A média é de: {media}")