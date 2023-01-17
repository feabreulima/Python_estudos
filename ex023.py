#Leia um número de 1 a 9999 e mostre seus algarismo separados

num = str(int(input('\nDigite um número de 0 a 9999: ')))

num = num + '000'

print(f'\nUnidade: {num[0]}')

print(f'Dezena: {num[1]}')

print(f'Centena: {num[2]}')

print(f'Milhar: {num[3]}\n')
