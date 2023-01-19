#Leia três número e mostre o maior e menor deles

n1 = float(input('Insira um número: '))
n2 = float(input('Insira um número: '))
n3 = float(input('Insira um número: '))

#Analisando os maiores
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print(f'\nO maior número é o {maior}')
#Analisando os menores
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f'O menor número é o {menor}\n')
    
if n1 == n2 or n2 == n3 or n1 == n3:
    print('\nHá valores iguais.')
