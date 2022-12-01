#math.fmod()
#Return , conforme definido pela biblioteca da plataforma C. Observe que a expressão Python pode não
#retornar o mesmo resultado. A intenção do padrão C é ser exatamente (matematicamente; com precisão infinita)
# igual a para algum número inteiro n tal que o resultado tenha o mesmo sinal de x e magnitude menor que .
# Python retorna um resultado com o sinal de y e pode não ser exatamente computável para argumentos float.
# Por exemplo, is , mas o resultado do Python é , que não pode ser representado exatamente como um float, e
# arredonda para o surpreendente .
# Por esta razão, funcionafmod(x, y)x % yfmod(x, y)x - n*yabs(y)x % yfmod(-1e-100, 1e100)-1e-100-1e-100 % 1e1001e100-1e-1001e100fmod()
# é geralmente preferido ao trabalhar com floats, enquanto o Python é preferido ao trabalhar com inteiros.x % y

#simplificando..... """ Retorne o restante de x/y: """ fonte https://www.w3schools.com/python/ref_math_fmod.asp

import math

print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))
print(math.fmod(0, 0))