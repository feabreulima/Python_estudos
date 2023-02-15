#Crie um programa que tenha uma tupla com várias palavras (sem acentos). Depois disso, mostre todas as vogais em cada palavra

palavras = ('Programar','Estudar','Treinar','Pilotar','Python','Excuseme','Curso')

for c in palavras:
    print(f"\nNa palavra {c} temos ", end='')
    for i in c.lower():
        if i in 'aeiou':
            print(i, end=' ')        
print('\n')
    