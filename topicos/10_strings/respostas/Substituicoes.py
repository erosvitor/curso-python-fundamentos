#!python3

texto = "0001;Siclano Pereira Alves;10-05-2000;(41)998885453;siclano@gmail.com;"
texto = texto.replace("(", "")
texto = texto.replace(")", "")
texto = texto.replace("-", "/")
texto = texto.upper()

print(texto)
