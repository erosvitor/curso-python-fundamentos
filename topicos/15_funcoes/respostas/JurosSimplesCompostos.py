#!python3

def calcularJurosSimples(capital, taxa, periodo):
  return capital * (taxa/100) * periodo

def calcularJurosCompostos(capital, taxa, periodo):
  taxa /= 100
  return capital * (1 + taxa) ** periodo

print("Calcular Juros Simples e Compostos")
print("")

capital = input("Informe o capital: ")
capital = float(capital)

taxa = input("Informe a taxa: ")
taxa = float(taxa)

periodo = input("Informe o periodo: ")
periodo = int(periodo)

tipoJuros = input("Deseja calcular Juros Simples ou Composto (S/C)?")

if tipoJuros == "S":
  juros = calcularJurosSimples(capital, taxa, periodo)
  print("Juros calculado: ", juros)
elif tipoJuros == "C":
  juros = calcularJurosCompostos(capital, taxa, periodo)
  juros = juros - capital
  print("Juros calculado: ", juros)
else:
  print("Tipo inválido")

