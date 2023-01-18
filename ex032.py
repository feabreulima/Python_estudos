#Leia um ano e diga se ele é um ano bissexto
from datetime import date

ano = int(input('\nDigite um ano a ser analisado ou insira 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano %4 != 0:                                         #if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:
    print(f'\nO ano de {ano} não é bissexto.\n')        #poderia ser usado (and,or) *menos linhas
else:
    if ano %100 != 0:
        print(f'\nO ano de {ano} é bissexto!\n')
    else:
        if ano %400 == 0:
            print(f'\nO ano de {ano} é bissexto!\n')
        else:
            print(f'\nO ano de {ano} não é bissexto.\n')
