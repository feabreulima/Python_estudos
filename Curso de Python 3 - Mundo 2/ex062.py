#Refaça o desafio 61 perguntando ao usuário se ele quer mais termos. Caso queria encerrar escolha 0 termos

print("=-"*20,"Progressão Aritmética","=-"*20)

p = int(input('\nDigite o valor do 1º termo: '))
r = int(input('Digite o valor da razão: '))
f = 9
c = 0

print("\nA sequência da P.A. é:\n")
print(p, end=' ')
while c != f:
    x = p+r
    print(x, end=" ")
    p = x
    c += 1
    if c == 9:
        mais = int(input('\n\nQuer mostrar mais quantos termos? '))
        if mais != 0:
            c += -mais
        else:
            print('\nFim do programa.\n')
