#math.frexp()
#Retorne a mantissa e o expoente de x como o par . m é um float ee é um inteiro tal que exatamente.
#Se x for zero, retorna , caso contrário . Isso é usado para “separar” a representação interna de um
#flutuador de maneira portátil.(m, e)x == m * 2**e(0.0, 0)0.5 <= abs(m) < 1

#Encontre a mantissa e o expoente de um número:

import math

print(math.frexp(4))
print(math.frexp(-4))
print(math.frexp(7))