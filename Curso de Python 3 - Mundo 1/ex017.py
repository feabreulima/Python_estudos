#Calcular pitágoras no triângulo retângulo

import math

catOp = int(input('\nDigite o comprimento do cateto oposto: '))

catAdj = int(input('Digite o comprimento do cateto adjacente: '))

hip = math.hypot(catOp , catAdj)

print(f'\nO comprimento da hipotenusa correspnde a: {math.ceil(hip)}')