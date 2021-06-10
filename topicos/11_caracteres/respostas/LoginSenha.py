#!python3

print("Login e Senha")
print("")
    
login = input("Digite o login: ")
senha = input("Digite a senha: ")
    
if login == senha:
  print("Login e Senha não podem ser iguais.")
elif len(login) < 5 or len(login) > 15:
  print("O login deve ter entre 5 e 15 caracteres")
elif len(senha) < 5 or len(senha) > 15:
  print("A senha deve ter entre 5 e 15 caracteres")
else:
  temDigitoNumerico = False
  temLetraMaiuscula = False
  
  for i in range(0, len(senha)):
    caractere = senha[i]
    if caractere.isdigit():
      temDigitoNumerico = True
      continue
    if caractere.isupper():
      temLetraMaiuscula = true
  
  if temDigitoNumerico and temLetraMaiuscula:
    print("Login e Senha válidos")
  else:
    print("A senha deve ter pelo menos um dígito e pelo menos uma letra maiúscula.")
