# exercícios py.
# william pena forte 23-11-2022.

# crie um programa q leia quanto dinheiro uma pesosa tem na carteira e mostre quantos dolares ela pode comprar. 
# considere USS1,00 = RS5,39

dolar = 5.3883  
print('Um Dolar esta custando USS {}'.format(dolar))

d = float(input('Informe o valor em dinheiro que você tem, para conversão R$'))

valor = d * dolar

print('Seu dinheiro e R${:.2f} e vale Uss{:.2f} '.format(d,valor))

