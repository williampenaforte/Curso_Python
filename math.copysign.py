#math.copysign

#Retorne o valor do primeiro parâmetro e o sinal do segundo parâmetro:

#Retorna um float com a magnitude (valor absoluto) de x , mas o sinal de y .
# #Em plataformas que oferecem suporte a zeros com sinal, retorna -1,0 .copysign(1.0, -0.0)

import math

print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))