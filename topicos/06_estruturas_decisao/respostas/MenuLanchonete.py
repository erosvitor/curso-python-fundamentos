#!python3

print("Menu lanchonete")
print("")
print("1 – X-Salada")
print("2 – X-Bacon")
print("3 – X-Egg")
print("4 – Refrigerante")
print("5 – Finalizar pedido")

item = input("Escolha um item do menu: ")
item = int(item)

if item == 1:
  print("Você escolheu X-Salada")
elif item == 2:
  print("Você escolheu X-Bacon")
elif item == 3:
  print("Você escolheu X-Egg")
elif item == 4:
  print("Você escolheu Refrigerante")
elif item == 5:
  print("Você escolheu finalizar pedido")
else:
  print("Item inexistente")
