#Fça um programa para jogar par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas no final do jogo.

from random import randint

print('-'*20)
print('Jogo do PAR ou ÍMPAR')
print('-'*20)

vit = 0

while True:
    pc = randint(0,10) #Computador escolhe
    
    user = int(input('\nEscolha um valor: ')) #Usuário escolhendo
    escl = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    while escl not in ['P','I']:
        escl = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    
    soma = (user + pc)
    
    if soma %2 == 0:
        pi = 'PAR'
        print(f'\nVocê jogou {user} e o computador {pc}. Total {soma} deu {pi}')
        if escl == 'P':
            vit += 1
            print(f'\nVocê VENCEU! Vamos jogar novamente...')
        else:
            break
    else:
        pi = 'IMPAR'
        print(f'\nVocê jogou {user} e o computador {pc}. Total {soma} deu {pi}')
        if escl == 'I':
            vit += 1
            print(f'\nVocê VENCEU! Vamos jogar novamente...')
        else:
            break
print(f'\nVocê PERDEU!\n\nVocê ganhou {vit} vezes.')
print('=-'*30)
