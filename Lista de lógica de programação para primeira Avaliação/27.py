kmpd = float(input("Quantidade de Km percorridos: "))  # Solicita a quantidade de Km percorridos
dal = int(input("Quantidade de dias alugados: "))  # Solicita a quantidade de dias alugados

preçopd = 90  # Preço por dia de aluguel
preçopkm = 0.20  # Preço por Km percorrido

valor = (kmpd * preçopkm) + (dal * preçopd)  # Calcula o valor total a pagar

print(f"Preço total a pagar: R${valor}")  # Exibe o valor total a pagar