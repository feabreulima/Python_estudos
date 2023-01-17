#Lê o nome de uma cidade e analisa se há o nome 'SANTO'

cidade = input('Insira o nome da cidade: ')
dividida = cidade.strip().upper().split()

print(f'A cidade começa com Santo?')
print('SANTO' in dividida[0])
