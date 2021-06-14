#!python3

import os

diretorioBase = "/home/erosvitor"

diretorioDocs = diretorioBase + "/docs"

os.mkdir(diretorioDocs)
os.chdir(diretorioDocs)

os.makedirs("gerencia/financeira")
os.makedirs("gerencia/administrativa")

os.makedirs("publico/fotos")
os.makedirs("publico/manuais")

arquivoResponsaveis = open(diretorioDocs + "/gerencia/responsaveis.txt", "w")
arquivoResponsaveis.write("Fulano da Silva\n")
arquivoResponsaveis.write("Beltrano Gomes\n")
arquivoResponsaveis.write("Siclano Cunha\n")
arquivoResponsaveis.close()

arquivoDescricao = open(diretorioDocs + "/publico/descricao.txt", "w")
arquivoDescricao.write("Diretório 'fotos'\n")
arquivoDescricao.write("Destinado ao armazenamento de fotos de eventos, comemorações e feiras\n")
arquivoDescricao.write("\n")
arquivoDescricao.write("Diretório 'manuais'\n")
arquivoDescricao.write("Destinado ao armazenamento de manuais dos produtos comercializados pela empresa.\n")
arquivoDescricao.close()

