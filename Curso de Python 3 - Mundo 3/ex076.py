#Crie um programa com uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final mostre uma listagem dos preços organizando os dados de forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"Listagem de Preços":^40}')
print('-'*40)

c = 0
v = 1
while c != 18:
    print(f'{produtos[c]:>12}{"..................R$":<0}{produtos[v]:>8}')
    c += 2
    v += 2
print('')
