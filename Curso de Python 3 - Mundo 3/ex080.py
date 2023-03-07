#Crie um programa que receba 5 valores numa lista e ordene-os sem usar o 'sort()'. Mostre a lista na tela ao final
List = []
cont = 0
print('')
for c in range(0,5):
    num = int(input('Digite um número: '))
    if c == 0:
        List.append(num)
        print("Adicionado no final da lista...")
    else:
        for i, x in enumerate(List):
            if num > List[i]:
                cont += 1
        if num > List[-1]:
            print("Adicionado no final da lista...")
        else:
            print(f'Adicionado na posição {cont} da lista...')
        List.insert(cont,num)
        cont = 0
                                
print('=-'*28,"\nOs valores digitados e ordenados são",List,'\n')
