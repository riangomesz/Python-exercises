print("Tipos de Triângulos")

l1 = int(input("\nDigite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
  print("\nForma um triângulo",end="")
  if l1 == l2 == l3:
    print(" Equilátero")
  elif l1 != l2 != l3 != l1:
    print(" Escaleno")  
  else:
    print(" Isóceles")
else:
  print("Não forma um triângulo")