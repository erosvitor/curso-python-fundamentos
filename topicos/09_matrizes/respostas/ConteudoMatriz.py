#!python3

print("Mostra conteúdo de uma matriz")
print("")

matriz = []

for i in range(0, 2):
  linha = []
  for j in range(0,2):
    valor = input(f"Digite o elemento para a posição {i},{j} da matriz: ")
    linha.append(int(valor))
  matriz.append(linha)

for linha in matriz:
  for item in linha:
    print(item)
