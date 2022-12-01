#william pena forte desafios curso em video python 30/11/2022

#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#exemplo digite um numero:. 6.127 --- O numero 6.127 tem a parte inteira 6
#dica ver todas as classes do modulo "math"

#import math

from math import trunc
from math import floor

n = float(input('informe um numero de ponto flutuante:. '))
nn = floor(n) #obs tive o mesmo resultado!
#nn = trunc(n)

print('o valor digitado foi {} e sua porção inteira e {}'.format(n,nn))





