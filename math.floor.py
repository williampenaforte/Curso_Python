#math.floor
#Retorna o piso de x , o maior inteiro menor ou igual a x . Se x não for float,
#delega para x.__floor__, que deve retornar um Integralvalor.

#Arredonde os números para o inteiro mais próximo:

import math

print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(5.8))
print(math.floor(-5.3))
print(math.floor(22.6))
print(math.floor(10.0))