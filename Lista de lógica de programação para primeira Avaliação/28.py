cig = int(input("Quantidade de cigarros fumados por dia: "))  # Solicita a quantidade de cigarros fumados por dia
anos = int(input("Quantos anos ele já fumou: "))  # Solicita quantos anos a pessoa já fumou

total = cig * 365 * anos  # Calcula o total de cigarros fumados em todos os anos
minp = total * 10  # Calcula o total de minutos perdidos de vida
diasp = minp / (24 * 60)  # Calcula o total de dias perdidos de vida

print(f"Esse fumante perdeu aproximadamente {diasp:.1f} dias de vida.")  # Imprime a quantidade de dias perdidos de vida