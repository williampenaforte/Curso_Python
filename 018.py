'''

william pena forte desafios curso em video python 30/11/2022

faca um progama que leia um angulo qualquer e mostre na tela o valor do seno, cosseo e
tangente desse angulo. Dica ver todas as classes do modulo "math"

'''

import math
ângulo = float(input('Digite o ângulo que vc deseja '))
seno = math.sin(math.radians(ângulo))
print('O angulo de {} tem o SENO de {:.2F}'.format(ângulo,seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo,cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo,tangente))
