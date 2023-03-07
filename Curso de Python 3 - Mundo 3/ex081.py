#Crie um programa que leia vário números e coloque-os numa lista. Depois mostre: a) quantos valores foram digitados b)A lista de valores ordenada de forma decrescente c)Se o 5 foi digitado e está na lista ou não

valores = []
print('')
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'\nVocê digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores,reverse=True)}')
if valores.count(5) == 1:
    print(f'O valor 5 está na lista, na posição {valores.index(5)}\n')
else:
    print('O valor 5 não está na lista.\n')
