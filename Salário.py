# Define the input variables
print ("------------- Calculadora --------------")

vl = float(input("Digite o valor ganho por hora: "))
h = float(input("Digite a quantidade de horas trabalhadas por mês:"))
d = 14/100

print (f"O seu salário líquido é de {(vl * h) - (vl * h) * (14/100)}R$")