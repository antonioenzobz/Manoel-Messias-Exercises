x = int(input("Digite um valor, e serão listados os números primos até o mesmo: "))

primos = []

# Loop para verificar se cada número é primo
for num in range(1, x+1):
  if num > 1:
    # Loop para verificar se o número é divisível por algum outro número
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      # Se o número não for divisível por nenhum outro número, ele é primo
      primos.append(num)

print("Números primos até", x, ":", primos)