#!python3

print("Login")
print("")

loginValido = False

while not loginValido:
  login = input("Digite o login: ")
  if login.strip():
    print("Login válido.")
    loginValido = True
  else:
    print("Login inválido, tente novamente.")
    loginValido = False
