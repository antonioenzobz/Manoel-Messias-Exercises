x = int(input("Digite sua idade em dias: "))  # Solicita a idade em dias ao usuário

anos = x // 365  # Calcula a quantidade de anos completos
x %= 365  # Atualiza o valor de x para o restante dos dias
meses = x // 30  # Calcula a quantidade de meses completos
dias = x % 30  # Calcula o restante dos dias

print(f"Sua idade corresponde a {anos} anos, {meses} meses e {dias} dias.")  # Imprime a idade em anos, meses e dias