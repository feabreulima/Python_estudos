#Crie uma matriz de dimensão 3x3 e preencha-a com valores lidos pelo teclado. No final mostre na tela com a formatação correta.

matriz = []
temp = []

i = 0
y = 0
x = 0

while y < 3:
    for x in range(3):
        if x > 2:
            x = 0
        num = int(input(f'Digite um valor para [{y},{x}]: '))
        temp.append(num)
        x += 1
    matriz.append(temp[:])
    temp.clear()
    y += 1
for valores in matriz:
    for v in valores:
        print(f'[ {v} ]', end=' ')
    print()
    
