#Leia um número inteiro e diga se ele é ou não um número primo
print('==-'*15,"Verificador de Nºs Primos",'-=='*15)
n = int(input('\nDigite um número inteiro maior que > 1: '))
print('')

for c in range(2,n+1):
    np = n % c
    if np == 0 and c != n:
        print(f'\n\033[4;31mO número {n} não é primo.\033[m\n')
        break
    if c == n and np == 0:
        print(f'\n\033[4;32mO número {n} é PRIMO!\033[m\n')
