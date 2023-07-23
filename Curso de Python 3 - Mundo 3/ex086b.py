#   Versão melhorada

matriz = []
temp = []
for y in range(0, 3):
    temp.clear()
    matriz.append(temp[:])
    for x in range(0, 3):
        num = int(input(f'Digite um valor para [{y},{x}]: '))
        matriz[y].append(num)
for y in range(0,3):
    for x in range(0, 3):
        print(f'[{matriz[y][x]:^5}]', end=' ')
    print()
        