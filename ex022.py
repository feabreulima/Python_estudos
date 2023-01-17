#Manipulação de texto

nome = input('\nDigite seu nome: ')

maiusculo = nome.strip().upper()
print(f'\nNome em caracteres maiúsculos: {maiusculo}')

minusculo = nome.strip().lower()
print(f'Nome em caracteres minúsculos: {minusculo}')

noespaco = nome.strip().replace(' ', '')
print(f'\nQuantas letras existe no nome: {len(noespaco)}')

dividido = nome.strip().split()
print(f'Quantas letras tem o primeiro nome: {len(dividido[0])}\n')
