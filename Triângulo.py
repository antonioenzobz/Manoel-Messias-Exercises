a = float(input("Digite o lado a:" ))
b = float(input("Digite o lado b:" ))
c = float(input("Digite o lado c:" ))

if a<b+c and b<a+c and c<a+b:
  if a==b==c:
    print ("O triângulo é equilátero!")
  elif a==b or b==c or a==c:
    print("O triângulo é isóceles!")
  else:
    print ("O triângulo é escaleno!")
else:
  print("Entrada inválida!")