#Leia o ano de nascimento de 7 pessoas e mostre quantas pessoas ja atinjiram a maioridade e quantos não atinjiram ainda

from datetime import date

maior = 0
menor = 0

for c in range(1,8):
    idade = date.today().year - int(input('\nQual seu ano de nascimento? '))
    print(f'\nIdade atual: {idade} anos')
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1

print(f"\nHá {maior} pessoas que atinjiram a maioridade. \nHá {menor} pessoas que NÃO atinjiram a maioridade.\n")
