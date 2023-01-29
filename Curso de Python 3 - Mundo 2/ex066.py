#Refaça o desafio 64 com os recursos break e while True

soma = qnt = 0

while True:
    n = int(input('\nDiigte um Nº inteiro ou [999 para parar]: '))
    if n == 999:
        break
    soma += n
    qnt += 1
print(f'\nFim do programa.\n\nForam digitados {qnt} números e a soma entre eles é {soma}\n')
