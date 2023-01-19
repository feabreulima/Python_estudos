import math
#Porção inteira de um número

num = float(input('\nDigite um número: '))

print(f'O número {num} é em porção inteira (mais próximo): {round(num)}\n')

print(f'O número {num} é em porção inteira (para baixo): {math.floor(num)}\n')

print(f'O número {num} é em porção inteira (para cima): {math.ceil(num)}')