#Manipulação de texto
cores = {
    'limpa': '\033[m',
    'azulSub': '\033[4;34m'
}

nome = input('\nDigite seu nome: ')

maiusculo = nome.strip().upper()
print(f"\nNome em caracteres maiúsculos: {cores['azulSub']}{maiusculo}{cores['limpa']}")

minusculo = nome.strip().lower()
print(f"Nome em caracteres minúsculos: {cores['azulSub']}{minusculo}{cores['limpa']}")

noespaco = nome.strip().replace(' ', '')
print(f"\nQuantas letras existe no nome: {cores['azulSub']}{len(noespaco)}{cores['limpa']}")

dividido = nome.strip().split()
print(f"Quantas letras tem o primeiro nome: {cores['azulSub']}{len(dividido[0])}{cores['limpa']}\n")
