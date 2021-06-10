#!python3

print("Lista de emails para mala direta")
print()

dados = [
  "Beltrano da Silva;beltrano@gmail.com", 
  "Siclano Goncalves;siclano@yahoo.com.br", 
  "Fulano Pereira Alves;fulanoalves@gmail.com", 
  "Alvarenga Pedroso;pedroso@hotmail.com"
]

emails = []

for linha in dados:
  posicaoDoCorte = linha.find(";") + 1
  emails.append(linha[posicaoDoCorte:])

for email in emails:
  print(email)
