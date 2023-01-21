#Leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos
print("=-"*20,"Progressão Aritmética","=-"*20)
p = int(input('\nDigite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))

print('\nA sequência da P.A. é:\n')
for c in range(p,r*10+p,r):
    print(c)
print('')
