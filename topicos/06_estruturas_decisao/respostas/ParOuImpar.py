#!python3

print("Verificar se um número é par ou ímpar")
print("")

numero = input("Digite um número inteiro maior que zero: ")
numero = int(numero)

if numero % 2 == 0:
  print("O número é PAR")
else:
  print("O número é ÍMPAR")
