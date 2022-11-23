#exercicios py
#william 23-11-22

# faca um algoritimo que leia o preço de uma produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('qual o preço o preço do produto? R$'))
desconto = 5
porcentagem = 100

resultado = preco - (preco*desconto/porcentagem)

print('O produto custava R${:.2f} e com desconto de 5% agora vale {:.2f}'.format(preco,resultado))
