#!python3

def nomeEhValido(nome):
  nomeValido = True
  for i in range(0, len(nome)):
    caractere = nome[i]
    if (not caractere.isalpha()) and (not caractere.isspace()):
      nomeValido = False
      break
  return nomeValido

def telefoneEhValido(telefone):
  telefoneValido = True
  for i in range(0, len(telefone)):
    caractere = telefone[i]
    if (not caractere.isdigit()) and (caractere != "-"):
      telefoneValido = False
      break
  return telefoneValido

print("Cadastro de Funcionário")
print("")

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
dataNascimento = input("Digite a data nascimento: ")

if not nomeEhValido(nome):
  print("Nome informado não é um nome válido.")
  exit(1)

if not telefoneEhValido(telefone):
  print("Telefone informado não é um telefone válido.")
  exit(1)

print("Cadastro efetuado com sucesso!")

