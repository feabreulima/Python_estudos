#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre: a) quantas vezes apareceu o valor 9
#b) em que posição foi digitado o primeiro valor 3 c)quais foram os números pares

tupla = (int(input('\nDigite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print(f'\nVocê digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição' if 3 in tupla else 'O 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram',end=' ')

c = 0
pares = []

for c in tupla:
    if c %2 == 0:
        print(c,end=' ')
