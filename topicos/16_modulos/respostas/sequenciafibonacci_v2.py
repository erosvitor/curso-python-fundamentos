#!python3

import fibonacci

fibonacci_arq = open("fibonacci.txt", "w")

for seq in [5, 10, 15]:
  sequencia = fibonacci.return_fib_series(seq)
  fibonacci_arq.write(",".join(str(n) for n in sequencia) + "\n")

fibonacci_arq.close()
