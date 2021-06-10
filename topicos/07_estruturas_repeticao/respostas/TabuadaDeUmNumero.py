#!python3

print("Tabuada de um número")
print("")

numero = input("Digite um número inteiro entre 1 e 10: ")
numero = int(numero)

for i in range(1, 11):
  print(f"{numero} x {i} = {numero*i}")
