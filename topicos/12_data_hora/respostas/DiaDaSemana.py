#!python3

from datetime import datetime

print("Dia da semana que o usuário nasceu")
print()

dataNascimentStr = input("Digite a sua data de nascimento: ")

dataNascimento = datetime.strptime(dataNascimentStr, "%d/%m/%Y")
diaSemana = dataNascimento.weekday()
    
nomeDiaSemana = ""
if diaSemana == 0:
  nomeDiaSemana = "Segunda-feira"
elif diaSemana == 1:
  nomeDiaSemana = "Terça-feira"
elif diaSemana == 2:
  nomeDiaSemana = "Quarta-feira"
elif diaSemana == 3:
  nomeDiaSemana = "Quinta-feira"
elif diaSemana == 4:
  nomeDiaSemana = "Sexta-feira"
elif diaSemana == 5:
  nomeDiaSemana = "Sábado"
else:
  nomeDiaSemana = "Domingo"

if diaSemana <= 4:
  print("Você nasceu numa ", nomeDiaSemana)
else:
  print("Você nasceu num ", nomeDiaSemana)
