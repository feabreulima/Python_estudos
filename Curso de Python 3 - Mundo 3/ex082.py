#Cire um programa que irá ler vários números e coloque-os numa lista. Depois crie duas listas extras apenas para valores ímpares e pares digitados, respectivamente. Ao final mostre as três listas geradas.

valores = []
pares = []
impares = []

while True:
    n = int(input('Diigite um valor: '))
    valores.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for c in valores:
    if c %2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('=-'*30)
print(f'A lista completa é {valores}\nA lista de pares é {pares}\nA lista de ímpares é {impares}\n')
