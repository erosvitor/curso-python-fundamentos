#!python3

print("Calcular preço consumidor")
print("")

porcentagemDistribuidor = 28/100
impostos = 45/100

custoFabrica = input("Informe o custo de fábrica: ")
custoFabrica = float(custoFabrica)

precoConsumidor = custoFabrica + (custoFabrica * porcentagemDistribuidor)
precoConsumidor = precoConsumidor + (precoConsumidor * impostos)

print("O preço consumidor é de ", precoConsumidor)

