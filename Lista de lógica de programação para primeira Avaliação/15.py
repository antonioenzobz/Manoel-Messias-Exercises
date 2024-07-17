print("------------- Calculadora de IMC --------------")

# Solicita ao usuário o peso e a altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcula o IMC
IMC = peso / (altura**2)

# Exibe o valor do IMC com duas casas decimais
print(f"O seu IMC é de {IMC:.2f}")

# Verifica a faixa de peso com base no IMC
if IMC < 18.5:
  print("Abaixo do peso")
elif IMC >= 18.6 and IMC <= 24.9:
  print("Peso ideal (parabéns)")
elif IMC >= 25.0 and IMC <= 29.9:
  print("Levemente acima do peso")
elif IMC >= 30.0 and IMC <= 34.9:
  print("Obesidade grau I")
elif IMC >= 35.0 and IMC <= 39.9:
  print("Obesidade grau II (severa)")
elif IMC >= 40:
  print("Obesidade grau III (mórbida)")