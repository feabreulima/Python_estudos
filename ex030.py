#Leia um número inteiro e mostre se ele é par ou ímpar

num = int(input('\nDigite um número inteiro: '))

if num % 2 == 0:
    print(f'\nO número {num} é par!\n')
else:
    print(f'\nO número {num} é ímpar!\n')