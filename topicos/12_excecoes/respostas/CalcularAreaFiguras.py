#!python3

def calcularAreaQuadrado():
  print("")
  lado = input("Digite o lado do quadrado: ")
  try:
    lado = float(lado)
    area = lado * lado
    print("A área do quadrado é ", area)
    print("")
  except ValueError:
    print("")
    print("O lado informado está incorreto")
    print("")

def calcularAreaTriangulo():
  print("")
  base = input("Digite a base do triângulo: ")
  altura = input("Digite a altura do triângulo: ")
  try:
    base = float(base)
    altura = float(altura)
    area = (altura * base) / 2
    print("A área do triângulo é ", area)
    print("")
  except ValueError:
    print("")
    print("O lado informado está incorreto")
    print("")

while True:
  print("1 - Calcular área quadrado")
  print("2 - Calcular área triângulo")
  print("3 - Finalizar")

  opcao = input("Digite a opção: ")
  if opcao == "1":
    calcularAreaQuadrado()
  elif opcao == "2":
    calcularAreaTriangulo()
  elif opcao == "3":
    break
  else:
    print("Opção inválida! Tente novamente")
    print("")
