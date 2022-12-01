#math.comb(n, k)
#Encontre o número total de possibilidades para escolher k itens de n itens:

#Retorne o número de maneiras de escolher k itens de n itens sem repetição e sem ordem.

#Avalia até quando e avalia como zero quando .n! / (k! * (n - k)!)k <= nk > n

#Também chamado de coeficiente binomial porque é equivalente ao coeficiente do k-ésimo termo na expansão polinomial de .(1 + x)ⁿ

#Aumenta TypeErrorse um dos argumentos não for inteiro. Aumenta ValueErrorse qualquer um dos argumentos for negativo.

import math

n = 7
k = 5

print(math.comb(n, k))
