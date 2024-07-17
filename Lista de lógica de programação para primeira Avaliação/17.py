ano = int(input("Digite um ano a ser verificado: "))

# Verifica se o ano é divisível por 4
if ano % 4 == 0:
  # Verifica se o ano não é divisível por 100 ou se é divisível por 400
  if ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto!")
  else:
    print(f"O ano {ano} não é bissexto!")