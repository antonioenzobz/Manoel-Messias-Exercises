# Imprime uma mensagem inicial explicando o propósito do programa
print("Determina se um numero é triangular\n")

# Solicita ao usuário que digite um valor para n e converte a entrada para um inteiro
n = int(input("Digite o valor de n: "))

# Inicializa a variável i com o valor 1
i = 1

# Este loop while verifica se o produto de três números consecutivos é menor que n
# O produto de três números consecutivos é representado por i * (i+1) * (i+2)
# O loop continua até encontrar um produto que seja igual ou maior que n
while i * (i+1) * (i+2) < n:
    # Incrementa i em 1 a cada iteração
    i = i + 1

# Após o loop, verifica se o produto de i, (i+1) e (i+2) é igual a n
if i * (i+1) * (i+2) == n:
    # Se for igual, imprime que n é um número triangular e mostra os três números que formam o produto
    print("%d é o produto %d*%d*%d" % (n, i, i+1, i+2))
else:
    # Se não for igual, imprime que n não é um número triangular
    print("%d nao é triangular" % (n))
