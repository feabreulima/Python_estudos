#Lê o nome de uma cidade e analisa se há o nome 'SANTO'

cidade = input('Insira o nome da cidade: ')
dividida = cidade.strip().upper().split()

print(f'\033[4;32mA cidade começa com Santo?\033[m')
print('SANTO' in dividida[0])
