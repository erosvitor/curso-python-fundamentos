#!python3

print("Calcular Juros Simples")
print("")

capital = input("Digite o capital: ")
taxa = input("Digite a taxa de juros (mensal): ")
periodo = input("Digite o período (em meses): ")

juros = float(capital) * (float(taxa)/100) * int(periodo)
print("O juros calculado foi de ", juros)
