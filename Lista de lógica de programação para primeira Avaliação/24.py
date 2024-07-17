# Solicita ao usuário os valores para os coeficientes da equação linear
a = float(input("Digite o valor A da equação linear:"))
b = float(input("Digite o valor b da equação linear:"))
c = float(input("Digite o valor c da equação linear:"))
d = float(input("Digite o valor d da equação linear:"))
e = float(input("Digite o valor e da equação linear:"))
f = float(input("Digite o valor f da equação linear:"))

# Calcula os valores de x e y utilizando as fórmulas da equação linear
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# Imprime os valores de x e y
print(f"O valor de x e y são respectivamente: {x} e {y}")