#!python3

print("Verificar a situção escolar de um aluno")
print("")

nota1 = input("Digite a nota do primeiro bimestre: ")
nota1 = float(nota1)
nota2 = input("Digite a nota do segundo bimestre: ")
nota2 = float(nota2)
nota3 = input("Digite a nota do terceiro bimestre: ")
nota3 = float(nota3)
nota4 = input("Digite a nota do quarto bimestre: ")
nota4 = float(nota4)

media = (nota1+nota2+nota3+nota4) / 4

if media >= 70.0:
  print("O aluno esta aprovado")
elif media < 40.0:
  print("O aluno esta reprovado")
else:
  print("O aluno esta em recuperação")
