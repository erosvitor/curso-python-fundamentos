#!python3

enderecosIP = open("/home/erosvitor/enderecosip.txt", "r")

enderecosClasseA = open("/home/erosvitor/enderecos-classe-a.txt", "w")
enderecosClasseB = open("/home/erosvitor/enderecos-classe-b.txt", "w")
enderecosClasseC = open("/home/erosvitor/enderecos-classe-c.txt", "w")

for endereco in enderecosIP.readlines():
  posicaoCorte = endereco.find('.')
  primeiroOcteto = endereco[0:posicaoCorte]
  primeiroOcteto = int(primeiroOcteto)

  if primeiroOcteto <= 126:
    enderecosClasseA.write(endereco)
  elif primeiroOcteto <= 191:
    enderecosClasseB.write(endereco)
  else:
    enderecosClasseC.write(endereco)

enderecosClasseC.close()
enderecosClasseB.close()
enderecosClasseA.close()

enderecosIP.close()
