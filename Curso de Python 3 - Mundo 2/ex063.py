#Escreva um programa que leia um número n mostre na tela os primeiros elementos de uma sequência de Fibonacci
print('-'*30)
print('Fibonnaci Sequence')
print('-'*30)
n = int(input('\nDigite um número inteiro: '))

c = 0
l = []
l.append(n)
l.append(n+1)

t = int(input('\nQuantos termos você quer mostrar? ')) - 2
print('')
print(n, end=" → ")
print(n+1, end=' → ')
while c != t:
    soma = l[-1] + l[-2]
    print(soma, end=' → ')
    l.append(soma)
    c += 1
print('\n')
