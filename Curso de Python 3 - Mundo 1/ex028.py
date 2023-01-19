#Gere um número aleatório entre 0 e 5 e peça para o usuário chutar um número. Anaise se ele venceu ou perdeu

import random

num = random.randint(1,4)
user = int(input('\nDigite um número inteiro entre 0 e 5: '))

if user == num:
    print(f'Você ganhou! O número era {num}\n')
if user != num:
    print(f'Você perdeu! O número era {num}\n')
if user > 4:
    print('Número inválido.\n')
if user <= 0:
    print('Número inválido.\n')