#william pena forte desafios curso em video python 30/11/2022

#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele , lendo o nome deles e escrevendo o nome do escolhido.

import random

a = str(input('Nome Primeiro Aluno:. '))
b = str(input('Nome Segundo Aluno:. '))
c = str(input('Nome Terceiro Aluno:. '))
d = str(input('Nome Quarto Aluno:. '))

lista = [a,b,c,d]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
