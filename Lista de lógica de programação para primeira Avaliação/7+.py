# Lista para armazenar os índices pluviométricos de cada dia
listaIP = []

# Loop para ler os índices pluviométricos de cada dia do mês de junho
for dia in range(1, 31):
  indice = float(input(f"Informe o índice pluviométrico do dia {dia}: "))
  listaIP.append(indice)

# Encontrar o dia que mais choveu
dia_mais_chuvoso = listaIP.index(max(listaIP)) + 1

# Encontrar o dia que menos choveu
dia_menos_chuvoso = listaIP.index(min(listaIP)) + 1

# Calcular as médias pluviométricas das duas quinzenas
media_quinzena1 = sum(listaIP[:15]) / 15
media_quinzena2 = sum(listaIP[15:]) / 15

# Exibir os resultados
print("--------------------------------------------------------------------")
print(f"O dia que mais choveu foi o dia: {dia_mais_chuvoso}")
print(f"O dia que menos choveu foi o dia: {dia_menos_chuvoso}")
print(f"A média pluviométrica da primeira quinzena foi: {media_quinzena1}")
print(f"A média pluviométrica da segunda quinzena foi: {media_quinzena2}")
print("--------------------------------------------------------------------")






