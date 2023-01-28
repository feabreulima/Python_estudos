#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar se o usuário quer ou não continuar digitando valores.

lista= []
x = 0
soma = 0
c = 0

while c != 1:
    num = int(input('\nDigite um Nº inteiro: '))
    x += 1
    soma += num
    lista.append(num)
    quest = str(input('\nQuer continuar? [Sim/Não]: ')).strip().upper()[0]
    
    if quest == 'N':
        print(f'\nA média dos valores digitados são {soma/x:.2f}')
        newl = sorted(lista)
        print(f'\nO maior valor digitado é {newl[-1]} e o menor é {newl[0]}\n')
        c = 1
        
    elif quest == 'S':
        c = 0
        
    else:
        x = 0
        soma = 0
        lista = []
        print('\nComando inválido. Programa reiniciado.')
    