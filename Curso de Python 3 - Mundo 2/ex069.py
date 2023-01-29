#Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada pergunte se quer continuar. Ao final mostre quantas pessoas tem menos de 18 anos;quantos homens foram cadastrados;quantas mulheres tem menos de 20 anos.

print('-'*20)
print('Cadastre uma pessoa')
print('-'*20)

mulherM20 = homem = idadeMaior = 0 

idade = int(input('\nIdade: '))
sexo = input('Sexo [M/F]: ').strip().upper()

while True:
    while sexo not in ['M', 'F']:
        sexo = input('Sexo [M/F]: ').strip().upper()
    if idade > 18:
        idadeMaior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherM20 += 1
        
    c = input('\nQuer continuar? [S/N] ').strip().upper()
    while c not in ['S', 'N']:
        c = input('\nQuer continuar? [S/N] ').strip().upper()
    if c == 'N':
        break
    else:
        print('-'*20)
        print('Cadastre uma pessoa')
        print('-'*20)
        idade = int(input('\nIdade: '))
        sexo = input('Sexo [M/F]: ').strip().upper()
        
print(f'\nTemos {idadeMaior} pessoas maiores de 18\nAo todo temos {homem} homens cadastrados\nE temos {mulherM20} mulheres com menos de 20\n')
