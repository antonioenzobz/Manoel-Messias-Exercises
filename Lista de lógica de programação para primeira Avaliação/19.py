valor = float(input("Digite o valor a ser cobrado: "))

# Verifica se o valor é divisível por 3
if valor % 3 == 0:
  # Se for divisível por 3, calcula o valor de entrada e as duas parcelas
  print(f"O valor de entrada será de {valor / 3}R$, e as duas parcelas no valor de {valor / 3}R$")
else:
  # Se não for divisível por 3, calcula o valor de entrada e as duas parcelas com porcentagens diferentes
  print(f"O valor de entrada será de {valor * 0.36}R$, e as duas parcelas de {valor * 0.32}R$")