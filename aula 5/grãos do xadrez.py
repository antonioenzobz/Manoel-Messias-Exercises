q = 0  # contador para o número de quadrados
g = 1  # quantidade inicial de grãos em um quadrado
total = 0  # contador para o total de grãos

while q < 64:
    q += 1
    total += g
    print(f"No quadrado {q} tem {g} grãos de trigo.")
    g += g

print(f"O somatório dos grãos é: {total}")