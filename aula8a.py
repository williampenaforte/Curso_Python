#exercios py william 28/11/2022

#-----------------------------------------------------------------------------------
#Primeiro exemplo importação.
#import math

#num = int(input('Digite um numero:. '))
#raiz = math.sqrt(num)

#print ('a raiz de {} é {}'.format(num,raiz))

#-----------------------------------------------------------------------------------
#Segundo exemplo importação.
#import math

#num = int(input('Digite um numero:. '))
#raiz = math.sqrt(num)

#print ('a raiz de {} é {}'.format(num, math.ceil(raiz) ))


#-----------------------------------------------------------------------------------
#Terceiro exemplo importação.
from math import sqrt

num = int(input('Digite um numero:. '))
#raiz = math.sqrt(num) #torna-se dispensavel esta linha
raiz = sqrt(num) #assim funciona.. com a linha acima nao funciona, pois mudou a forma como importar.. 
#neste formato importamos apenas o "sqrt"...

#print ('a raiz de {} é {}'.format(num, math.ceil(raiz) )) #tambem removido o ceil pois nao foi importado...
print ('a raiz de {} é {} '.format(num,raiz))


#-----------------------------------------------------------------------------------


