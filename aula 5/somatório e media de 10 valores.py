n = 1  # contador para controlar o número de valores inseridos
s = 0  # variável para armazenar a soma dos valores

while n <= 10:
    v = int(input("coloque um valor: "))  # solicita ao usuário que insira um valor
    s += v  # adiciona o valor inserido à soma total
    n += 1  # incrementa o contador

print(f"O somatório dos valores é: {s} e a média é: {s/10}")  # exibe o somatório e a média dos valores