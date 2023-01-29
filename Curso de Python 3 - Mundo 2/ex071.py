'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte quanto o cliente quer sacar (valor inteiro) e o programa
deve informar quantas e quais cédulas serão entregues (considere cédulas de 50,20,10 e 1 reais)'''

print('='*20)
print('     BANCO F')
print('='*20)

resto = c50 = c20 = c10 = c1 = 0

while True:
    saq = int(input('\nQual valor você quer sacar? R$ '))
    resto = saq %50
    
    