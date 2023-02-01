'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início pergunte quanto o cliente quer sacar (valor inteiro) e o programa
deve informar quantas e quais cédulas serão entregues (considere cédulas de 50,20,10 e 1 reais)'''
import math

print('='*30)
print('           BANCO F')
print('='*30)

while True: 
    
    saq = int(input('Qual valor você quer sacar? R$ '))
      
    c50 = math.floor(saq/50)
    if c50 > 0:
        print(f'\n{c50} cédulas de R$ 50')
    resto1 = math.floor(saq/50)*50
    resto2 = saq - resto1
    if resto2 == 0:
        break
        
    c20 = math.floor(resto2/20)
    if c20 > 0:
        print(f'{c20} cédulas de R$ 20')
    resto3 = math.floor(resto2/20)*20
    resto4 = resto2 - resto3
    if resto4 == 0:
        break
        
    c10 = math.floor(resto4/10)
    if c10 > 0:
        print(f'{c10} cédulas de R$ 10')
    resto5 = math.floor(resto4/10)*10
    resto6 = resto4 - resto5
    if resto6 == 0:
        break
        
    c1 = resto6//1
    print(f'{c1} cédulas de R$ 1')
    break
    
print('='*30)
print('TENHA UM BOM DIA!\n')
