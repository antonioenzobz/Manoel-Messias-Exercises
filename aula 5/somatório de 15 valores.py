n = 1  # contador para controlar o número de iterações
s = 0  # variável para armazenar o somatório dos fatoriais

while n <= 15:
  v = int(input("coloque um valor: "))  # solicita ao usuário um valor
  f = 1  # variável para armazenar o fatorial do valor inserido
  
  for i in range(1, v + 1):
    f *= i  # calcula o fatorial do valor inserido
    
  s += f  # adiciona o fatorial calculado ao somatório
  n += 1  # incrementa o contador de iterações

print(f"Somatório dos fatoriais: {s}")  # exibe o somatório dos fatoriais