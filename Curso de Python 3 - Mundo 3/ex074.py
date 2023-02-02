#Crie um programa que gere 5 números aleatórios e colocar numa tupla. Depois mostre a lista de nº gerados e indique
#o menor e o maior valor que estão na tupla
from random import randint

lista = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os valores sorteados foram {lista[0]} {lista[1]} {lista[2]} {lista[3]} {lista[4]}')
print(f'O menor valor foi: {min(lista)}\nE o maior valor foi: {max(lista)}\n')