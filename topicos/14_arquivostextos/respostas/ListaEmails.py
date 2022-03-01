#!python3

clientes = open("/home/erosvitor/clientes.txt", "r")

listaEmails = open("/home/erosvitor/lista-emails.txt", "w")

for cliente in clientes.readlines():
  dados = cliente.split(",")
  email = dados[2]
  # Remove possíveis espaços em branco
  email = email.strip()
  # Remove aspas simples
  email = email.replace("'", "")
  listaEmails.write(email + "\n")

listaEmails.close()
clientes.close()
