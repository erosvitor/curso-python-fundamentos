#!python3

print("Número Telefone Formatado")
print()
    
telefone = input("Digite um número de telefone: ")

telefoneSemFormatacao = ""
for i in range(0, len(telefone)):
  caractere = telefone[i]
  if caractere.isdigit():
    telefoneSemFormatacao += caractere
    
telefoneComFormatacao = ""
telefoneComFormatacao += "("
telefoneComFormatacao += telefoneSemFormatacao[0:2]
telefoneComFormatacao += ")"
    
telefoneComFormatacao += " "
    
telefoneComFormatacao += telefoneSemFormatacao[2:7]
telefoneComFormatacao += "-"
telefoneComFormatacao += telefoneSemFormatacao[7:11]

print(telefoneComFormatacao)
