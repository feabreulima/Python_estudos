#Faça um programa que mostre a tabuada de vários números que o usuário digitar. Encerre o programa quando o usuário inserir um número negativo.

v = 1

while True:
    v = 1
    t = float(input('\nDigite um Nº para ver sua tabuada [-1 para sair]: '))
    if t < 0:
        break
    while v != 11:
        print(f'\033[32m{t} x {v} = {t*v:.0f}\033[m')
        v +=1
print('\nFim.\n')
