#!python3

print("Valor Médio")
print("")

valores = []

for i in range(0, 5):
  valor = input(f"Digite o valor {i+1}: ")
  valores.append((int(valor)))

totalValores = 0
for valor in valores:
  totalValores += valor

valorMedio = totalValores / len(valores)

print("O valor médio é ", valorMedio)
