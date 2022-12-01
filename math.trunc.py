# math.trunc()
# Retorne x com a parte fracionária removida, deixando a parte inteira.
# Isso arredonda para 0: trunc()é equivalente a xfloor() positivo e equivalente a x negativo .
# Se x não for float, delega para , que deve retornar um valor.ceil()x.__trunc__Integral

#Encontre a parte inteira de diferentes números:

import math

print(math.trunc(2.77))
print(math.trunc(8.32))
print(math.trunc(8.77))
print(math.trunc(-99.29))
