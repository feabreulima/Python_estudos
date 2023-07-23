#Aprimoramento desafio anterior. a) soma de todos números pares b) soma de todos valores da terceira coluna c) o maior valor da segunda linha

matriz = []
temp = []

somaP = somaT = maiorS = 0

for y in range(3):
    matriz.append(temp[:])
    for x in range(3):
        matriz[y].append(int(input(f'Digite um valor para [{y},{x}]: ')))
print('-='*30)
for y in range(3):
    for x in range(3):
        print(f'[{matriz[y][x]:^5}]', end=' ')
        if matriz[y][x] %2 == 0:
            somaP += matriz[y][x]
        if x == 2:
            somaT += matriz[y][x]
        if y == 1:
            if x == 0:
                maiorS = matriz[y][x]
            elif matriz[y][x] > maiorS:
                maiorS = matriz[y][x]
    print()
print('-='*30)
print(f'A soma de todos os pares é {somaP}')
print(f'A soma de todos valores da terceira coluna é {somaT}')
print(f'O maior valor da segunda linha é {maiorS}\n')
