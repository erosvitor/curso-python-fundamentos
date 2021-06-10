#!python3

capital = 1000.00
taxa = 10
periodo = 1

juros = capital * (taxa/100) * periodo

print(f"O juros calculado sobre o capital de R$ {capital}, durante {periodo} mês, com uma taxa de {taxa}%, foi de R$ {juros}")
