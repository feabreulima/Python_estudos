#Leia um número de 1 a 9999 e mostre seus algarismo separados

num = str(int(input('\nDigite um número de 0 a 9999: ')))

num = num + '000'

cores = { 
         'r': '\033[4;35m',
         'g': '\033[4;32m',
         'v': '\033[4;31m',
         'azulSub': '\033[4;34m',
         'L': '\033[m'
         }

print(f"\nUnidade: {cores['azulSub']}{num[0]}{cores['L']}")

print(f"Dezena: {cores['v']}{num[1]}{cores['L']}")

print(f"Centena: {cores['g']}{num[2]}{cores['L']}")

print(f"Milhar: {cores['r']}{num[3]}{cores['L']}\n")
