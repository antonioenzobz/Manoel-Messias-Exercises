R = "s"  # Variável para controlar a repetição do programa

while R == "s":
  Salário = float(input("Qual o seu salário?: "))  # Solicita ao usuário que informe o salário

  if Salário <= 1500:
    print(f"Salário bruto: {Salário} ")
    print(f"Imposto devido (5%): {Salário * 0.05} ")
    print(f"Salário com desconto: {Salário - (Salário * 0.05)} ")

  elif Salário > 1500 and Salário <= 3000:
    print(f"Salário bruto: {Salário} ")
    print(f"Imposto devido (8%): {Salário * 0.08} ")
    print(f"Salário com desconto: {Salário - (Salário * 0.08)} ")
    
  elif Salário > 3000 and Salário <= 10000:
    print(f"Salário bruto: {Salário} ")
    print(f"Imposto devido (15%): {Salário * 0.15} ")
    print(f"Salário com desconto: {Salário - (Salário * 0.15)} ")
    
  elif Salário >= 15000:
    print(f"Salário bruto: {Salário} ")
    print(f"Imposto devido (27%): {Salário * 0.27} ")
    print(f"Salário com desconto: {Salário - (Salário * 0.27)} ")

  else:
    print("Valor inválido")
    
  R = input("Deseja continuar? (s/n): ")