#william pena forte desafios curso em video python 30/11/2022

#crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e
#mostre o comprimento da hipotenusa.
#dica ver todas as classes do modulo "math"

''' via matematica pura
co = float(input(('comprimento do catato oposto')))
ca = float(input('comprimento do catato adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('a hipotenusa vai valer {:.2f}'.format(hi)) #resultado de 2 por 2.5 = 3.20 via calculos matematicos...'''

#usando classes
import math
co = float(input(('comprimento do catato oposto')))
ca = float(input('comprimento do catato adjacente'))
hi = math.hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))



