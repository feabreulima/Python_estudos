#Melhore o desafio 28, deixando o usuário chutar números até acertar e mostrando o total de chutes

import random
num = random.randint(1,11)

tentativas = 0
user = int(input('\nDigite um número inteiro entre 0 e 10: '))
tentativas += 1
while user != num:
    user = int(input('\n\033[31mVocê errou!\033[m Tente novamente.\n\nDigite um número inteiro entre 0 e 10: '))
    tentativas += 1
print(f'\n\033[32mVocê acertou!\033[m Com {tentativas} tentativa(s)!\n')
