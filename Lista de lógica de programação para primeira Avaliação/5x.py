mensagem = input("Digite a mensagem a ser criptografada: ")  # Solicita ao usuário que digite a mensagem a ser criptografada
cripto = ""  # Variável para armazenar a mensagem criptografada
chave = int(input("Digite a chave de criptografia: "))  # Solicita ao usuário que digite a chave de criptografia

for letra in mensagem:  # Percorre cada letra da mensagem
  if letra.isalpha():  # Verifica se a letra é uma letra do alfabeto
    cripto += chr((ord(letra) - 97 + chave) % 26 + 97)  # Criptografa a letra e adiciona à mensagem criptografada
  else:
    cripto += letra  # Se não for uma letra do alfabeto, adiciona a letra à mensagem criptografada sem alterações

print(f"A mensagem criptografada é: {cripto}")  # Exibe a mensagem criptografada