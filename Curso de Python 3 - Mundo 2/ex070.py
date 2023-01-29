#Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário quer continuar. No final mostre o total gasto; quantos produtos custam mais de 1.000; qual o nome do produto mais barato
print('='*20)
print('LOJA')
print('='*20)

c = maisbarato = mil = total = 0
nomebarato = ' '

while True:
    nome = str(input('\nQual o nome do produto? ')).capitalize().strip()
    price = float(input('Digite o preço: R$ '))
    
    total += price #Calculando se o preço é maior que 1000
    if price > 1000:
        mil += 1
        
    c += 1 #Se houver apenas um item ele será o menor valor (maisbarato e nome dele)
    if c == 1:
        maisbarato = price
        nomebarato = nome
        
    if c != 1 and price < maisbarato: #Caso um novo item seja mais barato ele se torna o (maisbarato)
        maisbarato = price
        nomebarato = nome
        
    resp = ' '
    while resp not in 'SN': #Enquanto resposta for diferente (!=) de 'S' ou 'N' continue a perguntar
        resp = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
        
    if resp == 'N': #Se resposta recebe 'N' o programa encerra (break)
        break
    
print('\nFIM DO PROGRAMA\n')
print(f'\033[32mO total da compra foi R$ {total}\nTemos {mil} produtos custando mais de R$ 1.000,00\nE o produto mais barato foi {nomebarato} custando R$ {maisbarato}\033[m\n')
