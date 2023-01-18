#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input('\nQual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))

lista = (r1 , r2 , r3)          #if r1<r2 + r3 and r2<r1 + r3 and r3<r1 + r2:
x = sorted(lista)

maior = x[-1]
menor = x[0]
medio = x[1]

if medio >= (maior-menor+1):
    print(f'\nAs retas {menor} e {medio} podem formam um triângulo!\n')
else:
    print('\nAs retas não podem formar um triângulo.\n')
