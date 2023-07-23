#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha separados os valores ímpares e pares. No final mostre os valores pares e ímpares em ordem crescente.

principal = [[],[]]

for i in range(1,8):
    num = int(input(f'Digite o {i}º valor: '))
    
    if num %2 == 0:
        principal[0].append(num)
    else:
        principal[1].append(num)
print(f'\nOs valores pares digitados foram: {sorted(principal[0])}')
print(f'Os valores ímpares digitados foram: {sorted(principal[1])}\n')
