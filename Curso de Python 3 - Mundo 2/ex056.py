'''Faça um programa que leia o nome de 4 pessoas, idade e sexo.
Mostre a média das idades, o nome do homem mais velho e quantas mulheres tem idade menor que 20 anos'''

allf = []
allm = []
mvint = []
soma = 0

for c in range(1,5):
    nome = str(input(f"\nDigite o {c}º Nome: ")).capitalize().strip()
    idade = int(input('Idade: '))
    soma += idade
    sexo = str(input('Sexo: [M/F]: ')).upper()
    if sexo == 'F':
        allf.append(idade)
        if idade < 20:
            mvint.append(idade)
    elif sexo == 'M':
        allm.append(str(idade)+sexo+nome)
        
print(f"\nA média das quatro idades são {soma//4} anos.")
if allm:
    x = sorted(allm)
    if x[-1][1] == 'M':
        print(f"\nO nome do homem mais velho é {x[-1][2::]}")
    else:
        print(f"\nO nome do homem mais velho é {x[-1][3::]}")
        
print(f"\nHá {len(mvint)} mulheres com menos de vinte anos.\n")
