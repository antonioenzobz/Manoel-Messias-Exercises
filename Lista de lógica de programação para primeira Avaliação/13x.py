def validar_cnpj(cnpj):
  cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
  
  if len(cnpj) != 14:
    return False
  
  # Verifica se todos os dígitos são iguais
  if len(set(cnpj)) == 1:
    return False
  
  # Calcula o primeiro dígito verificador
  soma = 0
  peso = 5
  for i in range(12):
    soma += int(cnpj[i]) * peso
    peso -= 1
    if peso < 2:
      peso = 9
  
  digito1 = soma % 11
  if digito1 < 2:
    digito1 = 0
  else:
    digito1 = 11 - digito1
  
  # Calcula o segundo dígito verificador
  soma = 0
  peso = 6
  for i in range(13):
    soma += int(cnpj[i]) * peso
    peso -= 1
    if peso < 2:
      peso = 9
  
  digito2 = soma % 11
  if digito2 < 2:
    digito2 = 0
  else:
    digito2 = 11 - digito2
  
  # Verifica se os dígitos verificadores são iguais aos informados
  if int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2:
    return True
  else:
    return False

# Exemplo de uso
cnpj = input("Digite o CNPJ: ")
if validar_cnpj(cnpj):
  print("CNPJ válido")
else:
  print("CNPJ inválido")