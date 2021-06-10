#!python3

print("Temperatura mínima e máxima")
print("")

temperaturas = [27.8, 26.9, 24.7, 26.9, 25.8, 27.6, 23.0, 21.2, 29.1, 25.4]
tempMinima = 999.9
tempMaxima = 0.0

for temp in temperaturas:
  if temp < tempMinima:
    tempMinima = temp
  if temp > tempMaxima:
    tempMaxima = temp

print("Temperatura mínima: ", tempMinima)
print("Temperatura máxima: ", tempMaxima)
