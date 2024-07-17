def validar_cpf(cpf):
  # Remover caracteres especiais do CPF
  cpf = cpf.replace(".", "").replace("-", "")

  # Verificar se o CPF possui 11 dígitos
  if len(cpf) != 11:
    return False

  # Verificar se todos os dígitos são iguais
  if cpf == cpf[0] * 11:
    return False

  # Calcular o primeiro dígito verificador
  soma = 0
  for i in range(9):
    soma += int(cpf[i]) * (10 - i)
  digito1 = 11 - (soma % 11)
  if digito1 > 9:
    digito1 = 0

  # Calcular o segundo dígito verificador
  soma = 0
  for i in range(10):
    soma += int(cpf[i]) * (11 - i)
  digito2 = 11 - (soma % 11)
  if digito2 > 9:
    digito2 = 0

  # Verificar se os dígitos verificadores estão corretos
  if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
    return False

  return True

# Exemplo de uso
cpf = input("Digite o CPF: ")
if validar_cpf(cpf):
  print("CPF válido")
else:
  print("CPF inválido")