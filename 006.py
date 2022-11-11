# exercícios python
# william pena forte 11-11-2022

# fazer um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
# exp numero 8 -- antecessor 7 , num 8 , sucessor 9

# crie um altoritimo que leia um numero e mostre o seu dobro, triplo e sua raiz quadrada.
n = float(input('digite um numero: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {}'.format(n,d))
print('O triplo de {} vale {}'.format(n,t))
print('A Rais quadrada de {} e igual a {:.0f}'.format(n,r))
print('A Raiz quadrada de {} e igual a {:.1f}'.format(n,r))
print('A Raiz quadrada de {} e igual a {:.2f}'.format(n,r))
print('A Raiz quadrada de {} e igual a {:.3f}'.format(n,r))
print('A Rais quadrada de {} e igual a {}'.format(n,r))