#Calcule a soma de todos os números ímpares múltiplos de 3 (três) entre 1 e 500
soma = 0
print('\nA soma de todos os números ímpares entre 1 e 500 é:\n')
for c in range(0,501,3):
    if c %2 != 0:
        soma += c
print(soma,"\n")