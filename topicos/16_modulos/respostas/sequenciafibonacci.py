#!python3

import fibonacci

fibonacci_arq = open("fibonacci.txt", "w")

separador = ","

sequencia = fibonacci.return_fib_series(5)
fibonacci_arq.write(separador.join(str(n) for n in sequencia))
fibonacci_arq.write("\n")

sequencia = fibonacci.return_fib_series(10)
fibonacci_arq.write(separador.join(str(n) for n in sequencia))
fibonacci_arq.write("\n")

sequencia = fibonacci.return_fib_series(15)
fibonacci_arq.write(separador.join(str(n) for n in sequencia))

fibonacci_arq.close()

