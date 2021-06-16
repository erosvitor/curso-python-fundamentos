from datetime import datetime

def diaSemanaPorExtenso(diaSemana):
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
    nomeDiaSemana = "Sabado"
  elif diaSemana == 5:
    nomeDiaSemana = "Domingo"
  return nomeDiaSemana

def mesPorExtenso(mes):
  meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", 
           "setembro", "outubro", "novembro", "dezembro")

  return meses[mes-1] 

def dataPorExtenso(dataStr):
  data = datetime.strptime(dataStr, "%d/%m/%Y")

  diaSemana = data.weekday()
  nomeDiaSemana = diaSemanaPorExtenso(diaSemana)

  mes = data.month
  nomeMes = mesPorExtenso(mes)

  return f"{nomeDiaSemana}, {data.day} de {nomeMes} de {data.year}"
  
