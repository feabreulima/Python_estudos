#Faça o computador jogar jokenpô com você
import random

pc = random.randint(1,3)

if pc == 1:
    pc = 'Pedra'
elif pc == 2:
    pc = 'Papel'
else:
    pc = 'Tesoura'

print('=-'*20)
print(' '*13,'JOKENPÔ GAME')
print('=-'*20)

user = int(input('\nDigite:\n\n 1 - Para escolher Pedra \n 2 - Para escolher Papel \n 3 - Para escolher Tesoura   \n\n'))


if user == 1:
    user = 'Pedra'
    print(f"\n\033[1;34mO computador escolheu {pc} e você escolheu {user}\033[m")
elif user == 2:
    user = 'Papel'
    print(f"\n\033[1;34mO computador escolheu {pc} e você escolheu {user}\033[m")
elif user == 3:
    user = 'Tesoura'
    print(f"\n\033[1;34mO computador escolheu {pc} e você escolheu {user}\033[m")
else:
    print('\n\033[1;31mNúmero inválido\033[m\n')
    
#Empates
if pc == 'Pedra' and user == 'Pedra' or pc == 'Papel' and user == 'Papel' or pc == 'Tesoura' and user == 'Tesoura':
    print('\nDeu empate!\n')
#PC wins
elif pc == 'Pedra' and user == 'Tesoura' or pc == 'Papel' and user == 'Pedra' or pc == 'Tesoura' and user == 'Papel':
    print(f"\n\033[4;31mO computador ganhou de você\033[m.\n")
#Wins user
elif user == 'Pedra' and pc == 'Tesoura' or user == 'Papel' and pc == 'Pedra' or user == 'Tesoura' and pc == 'Papel':
    print(f"\n\033[4;32mVocê ganho!\033[m\n")
