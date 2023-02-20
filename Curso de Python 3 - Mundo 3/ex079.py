#Crie um programa onde o usuário possa digitar vário valores numéricos e cadastre-os em uma lista. Caso o número já exista, ele não será adicionado. No final, exiba os valores em ordem crescente; valores únicos

valores = []
print('')

while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'\nVocê digitou os valores {sorted(valores)}\n')
