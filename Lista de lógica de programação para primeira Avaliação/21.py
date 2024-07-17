Saldo = float(input("Digite o seu saldo médio do ano anterior: "))

# Verifica o saldo médio e determina o crédito correspondente
if Saldo >= 0 and Saldo <= 200:
  print("Você não possui crédito")
elif Saldo > 200 and Saldo <= 400:
  print(f"Você possui um crédito de: {Saldo*0.2}R$")
elif Saldo > 400 and Saldo <= 600:
  print(f"Você possui um crédito de: {Saldo*0.3}R$")
elif Saldo > 600:
  print(f"Você possui um crédito de: {Saldo*0.4}R$")
else:
  print("Entrada inválida!")