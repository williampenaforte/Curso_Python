#exercicios py.
#william 23-11-22.

# faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input('Qual o salario do funcionario? R$'))

n = salario + (salario*15/100)

print('O novo sario do funcionari e R${:.2f}'.format(n))
