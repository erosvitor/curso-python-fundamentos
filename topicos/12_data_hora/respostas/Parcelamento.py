#!python3

from datetime import date, datetime, timedelta

print("Parcelamento")
print()

dataAtual = date.today()

valorCompra = input("Digite o valor da compra: ")
valorCompra = float(valorCompra)
    
numeroParcelas = input("Deseja parcelar em quantas vezes (2-5)? ")
numeroParcelas = int(numeroParcelas)
    
valorParcelado = valorCompra / numeroParcelas
    
for i in range(0, numeroParcelas):
  dataAtual = dataAtual + timedelta(days=30)
      
  print(f"Parcela {(i+1)}: %.2f" % valorParcelado)
  print(f"Pagamento em: ", datetime.strftime(dataAtual, "%d/%m/%Y"))
