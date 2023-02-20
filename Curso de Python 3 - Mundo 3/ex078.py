#Faça um programa que leia 5 valores numéricos e guarde-os numa lista. No final mostre o maior e menor valor digitado e suas respectivas posições

lista = []

maior = menor = ''
cont = cont2 = 0

for c in range(0,5):
    lista.append(int(input(f'\nDigite um número para a posição {c}: ')))
print("\nVocê digitou os valores",lista)

for c, v in enumerate(lista):
    at1 = v
    if v == sorted(lista)[-1] and cont == 0:
        cont = 1
        maior = v
        print(f'\nO maior valor digitado foi {v} na posição {c}...', end='')
    elif at1 == maior:
        print(f'{c}...', end='')
    at1 = 0

for j, k in enumerate(lista):
    at2 = k
    if k == sorted(lista)[0] and cont2 == 0:
        cont2 = 1
        menor = k
        print(f'\nO menor valor digitado foi {k} na posição {j}...', end='')
    elif at2 == menor:
        print(f'{j}...', end='')
    at2 = 0
print('\n')
