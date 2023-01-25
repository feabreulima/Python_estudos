#Leia dois valores numéricos e mostre um menu de escolha ao usuário
v = 0
print('=-'*20)
print(' '*15,'MENU')
print('=-'*20)
while v != 1:
    n1 = float(input('\nDigite um valor: '))
    n2 = float(input('Digite o segundo valor: '))
    escolha = int(input('\n\033[34mDigite:\n\n[1] Para somar\n[2] Para multiplicar\n[3] Exibir o maior\n[4] Novos números\n[5] Sair do programa\033[m\n\n'))
    if escolha == 1:
        soma = n1 + n2
        print(f"\nA soma entre os dois valores é {soma}")
    elif escolha == 2:
        multi = n1 * n2
        print(f"\nA multiplicação entre os valores é {multi}")
    elif escolha == 3:
        if n1 > n2:
            print(f"\nO maior valor é {n1}")
        else:
            print(f"\nO maior valor é {n2}")
    elif escolha == 5:
        v = 1
print('\n\033[32mFim do programa.\033[m\n')
