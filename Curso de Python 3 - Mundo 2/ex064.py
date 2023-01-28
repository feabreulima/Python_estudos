#Crie um programa que leia vários números no teclado, o programa apenas irá parar se o número 999 for digitado (condição de parada). No final mostre quantos números foram digitados e qual a sua soma.

p = q = soma = 0

n = float(input('\nDigite um número (999 para parar): '))

while p != 1:
    if n != 999:
        soma += n
        q += 1
        n = float(input('\nDigite um número (999 para parar): '))
    else:
        p = 1
        print(f'\nForam digitados {q} números e a soma entre eles são {soma:.1f}')
        print('\nFim do Programa...\n')
