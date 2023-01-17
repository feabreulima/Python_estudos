#Verificar se uma pessoa tem 'Silva' no nome

name = str(input('\nDigite seu nome completo: ')).strip()
name2 = name.upper().split()

print('Tem Silva no seu nome?')
print('SILVA' in name2)
