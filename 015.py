# exercicios py, william 27-11-22

# escreva um programa que pergunte a quantidade de km percorridos por um carro e a quantidade de dias
# pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

print('Quanto tenho que pagar pelo aluguel de um carro?\nImforme os dados a baixo, para calculo.')

print('\n')

valor_diaria = 60.00
valor_km = 0.15

diaria = float(input('Qantos dias o carro ficou alugado?' ))
km = float(input('Quantos Km o carro rodou?' ))

custo_diaria = valor_diaria * diaria
custo_km = valor_km * km

total = custo_km + custo_diaria

print('\n')
print('A diaria custa R${}\nO Km rodado custa R${}\nVocê alugou o carro por {} Dias\nE Rorou {} KM\n'.format(valor_diaria,valor_km,diaria,km))
print('O valor a pagar e R${}'.format(total))

