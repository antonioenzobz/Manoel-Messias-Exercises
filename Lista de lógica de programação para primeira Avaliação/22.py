print("------------- CORDENADAS - PONTO 1 --------------")
x1 = int(input("Digite as coordenadas referentes ao ponto x1: ")) 
y1 = int(input("Digite as coordenadas referentes ao ponto y1: ")) 

print("------------- CORDENADAS - PONTO 2 --------------")
x2 = int(input("Digite as coordenadas referentes ao ponto x2: ")) 
y2 = int(input("Digite as coordenadas referentes ao ponto y2: ")) 

# Calcula a distância entre os pontos usando a fórmula da distância euclidiana
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

print(f"A distância entre os pontos é de: {d:.2f}")