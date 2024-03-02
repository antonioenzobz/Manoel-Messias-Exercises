n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

if 0>=n1<=10 and 0>=n2<=10 and 0>=n3<=10 and 0>=n4<=10:
  if ((n1+n2+n3+n4)/4) >= 7:
    print("Aprovado!")
  else:
    print ("Reprovado!")
    ef = float(input("Digite a sua nota do exame final: "))
    if ((n1+n2+n3+n4)/4) <= ef:
      print("Aprovado pelo exame final!")
    else:
      print("Reprovado pelo exame final!")
else:
  print("Entrada inválida")