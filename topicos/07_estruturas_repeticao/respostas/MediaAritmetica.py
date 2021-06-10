#!python3

print("Média Aritmética")
print("")

qtde = 1
nota = 0.0

somaDasNotas = 0.0
while qtde <= 4:
  nota = input(f"Digite a nota {qtde}:")
  nota = float(nota)
  somaDasNotas += nota
  qtde += 1

media = somaDasNotas / 4

print(f"A média aritmética é {media}")
