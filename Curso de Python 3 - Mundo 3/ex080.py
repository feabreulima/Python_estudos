#Crie um programa que receba 5 valores numa lista e ordene-os sem usar o 'sort()'. Mostre a lista na tela ao final
lista = []
cont = 0
print('')
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    if c == 1:
        if valor > lista[0]:
            lista.append(valor)
            print('Adicionado ao final da lista...')
        else:
            lista.insert(0,valor)
            print('Adicionado na posição 0 da lista...')
    if c == 2:
        if valor > lista[1]:
            lista.append(valor)
            print('Adicionado ao final da lista')
        elif valor > lista[0] and valor < lista[1]:
            lista.insert(1,valor)
            print('Adicionado na posição 1 da lista...')

        else:
            lista.insert(0,valor)
            print('Adicionado na posição 0 da lista...')
    if c == 3:
        if valor > lista[2]:
            lista.append(valor)
            print('Adicionado ao final da lista...')
        elif valor > lista[0] and valor < lista[1]:
            lista.insert(1,valor)
            print('Adicionado na posição 1 da lista...')
        elif valor > lista[1] and valor < lista[2]:
            lista.insert(2,valor)
            print('Adicionado na posição 2 da lista...')
        else:
            lista.insert(0,valor)
            print('Adicionado na posição 0 da lista...')
    if c == 4:
        if valor > lista[3]:
            lista.append(valor)
            print('Adicionado ao final da lista...')
        elif valor > lista[0] and valor < lista[1]:
            lista.insert(1,valor)
            print('Adicionado na posição 1 da lista...')
        elif valor > lista[1] and valor < lista[2]:
            lista.insert(2,valor)
            print('Adicionado na posição 2 da lista...')
        elif valor > lista[2] and valor < lista[3]:
            lista.insert(3,valor)
            print('Adicionado na posição 3 da lista...')
        else:
            lista.insert(0,valor)
            print('Adicionado na posição 0 da lista...')
print('=========================\n',"Os valores digitados foram",lista,'\n')
