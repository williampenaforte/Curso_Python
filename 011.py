# exercícios py
# william pena forte 23-11-2022

# faça um programa que leia a largura  e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Qual a largura? '))
altura = float(input('Qual a altura? '))
area = altura * largura
print('Sua parede tem a dimensão de {} x {} e sua area e de {} m².'.format(largura,altura,area))

tinta = area / 2
print ('Para pintar esta parede, você deve usar {}L de tinta '.format(tinta))