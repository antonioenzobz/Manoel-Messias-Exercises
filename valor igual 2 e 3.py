# Ler quatro valores inteiros
valor1 = int(input("Digite o 1º valor inteiro: "))
valor2 = int(input("Digite o 2º valor inteiro: "))
valor3 = int(input("Digite o 3º valor inteiro: "))
valor4 = int(input("Digite o 4º valor inteiro: "))

# Verificar os valores divisíveis por 2 e 3
if valor1 % 2 == 0 and valor1 % 3 == 0:
    print("Valor", valor1, "é divisível por 2 e 3")
if valor2 % 2 == 0 and valor2 % 3 == 0:
    print("Valor", valor2, "é divisível por 2 e 3")
if valor3 % 2 == 0 and valor3 % 3 == 0:
    print("Valor", valor3, "é divisível por 2 e 3")
if valor4 % 2 == 0 and valor4 % 3 == 0:
    print("Valor", valor4, "é divisível por 2 e 3")
