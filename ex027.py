#Leia um nome completo e mostre o primeiro e último nome de uma pessoa

name = input('\nDigite seu nome completo: ').strip()

list = name.split()

print(f'Seu primeiro nome é: {list[0]}')

print(f'Seu último nome e: {list[-1]}\n')
