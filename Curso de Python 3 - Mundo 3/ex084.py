#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre a) quantas pessoas foram cadastradas b) uma lista com as mais pesadas c) uma lista com as mais leves

temp = []
dados = []

maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso em Kg: ')))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'O maior peso foi de {maior} Kg, sendo de: ')
for p in dados:
    for peso in p:
        if peso == maior:
            print(p[0], end='; ')
print(f'\nO menor peso foi de {menor} Kg, sendo de:')
for p in dados:
    for peso in p:
        if peso == menor:
            print(p[0], end='; ')
