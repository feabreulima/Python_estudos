#Leia uma frase e diga se ela é um palíndromo (mesma frase lida de tras para frente)

frase = input('\nDigite uma frase: ').strip().replace(' ','')

c = frase[::-1]

if c in frase:
    print(f'\nA frase é um políndromo!\n')
else:
    print(f'\nA frase NÃO é um políndromo.\n')
