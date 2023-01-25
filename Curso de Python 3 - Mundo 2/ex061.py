#Refaça o desafio 51 usando o While

print("=-"*20,"Progressão Aritmética","=-"*20)

p = int(input('\nDigite o valor do 1º termo: '))
r = int(input('Digite o valor da razão: '))

c = 0

print("\nA sequência da P.A. é:\n")
print(p, end=' ')
while c != 9:
    x = p+r
    print(x, end=" ")
    p = x
    c += 1
print('\n')
