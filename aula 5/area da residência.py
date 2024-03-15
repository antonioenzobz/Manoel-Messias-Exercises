continuar = "s"  # Variável para controlar se o usuário deseja continuar adicionando cômodos
at = 0  # Variável para armazenar a área total da residência

while continuar == "s":
  nome = input("Digite o nome do cômodo: ")  # Solicita ao usuário o nome do cômodo
  largura = float(input("Digite a largura do cômodo: "))  # Solicita ao usuário a largura do cômodo
  altura = float(input("Digite a altura do cômodo: "))  # Solicita ao usuário a altura do cômodo
  area = largura * altura  # Calcula a área do cômodo
  print(f"A área do(a) {nome} é de: {area} m²")  # Exibe a área do cômodo
  continuar = input("Deseja continuar? (s/n) :")  # Pergunta ao usuário se deseja continuar adicionando cômodos
  at = at + area  # Atualiza a área total da residência somando a área do cômodo atual
  
print(f"A área total da residência é: {at} m²")  # Exibe a área total da residência