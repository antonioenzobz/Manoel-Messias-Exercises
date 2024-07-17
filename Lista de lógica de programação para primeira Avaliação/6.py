Pa = 5000000  # População inicial do país A
Pb = 7000000  # População inicial do país B
Ta = 0.03     # Taxa de crescimento anual da população do país A
Tb = 0.02     # Taxa de crescimento anual da população do país B
anos = 0      # Contador de anos

while Pa <= Pb:
  Pa += Pa * Ta  # Atualiza a população do país A com base na taxa de crescimento
  Pb += Pb * Tb  # Atualiza a população do país B com base na taxa de crescimento
  anos += 1     # Incrementa o contador de anos

print(f"Serão necessários {anos} anos para a população do país A ultrapassar a população de B.")