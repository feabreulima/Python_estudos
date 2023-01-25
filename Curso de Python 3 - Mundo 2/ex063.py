#Escreva um programa que leia um número n mostre na tela os primeiros elementos de uma sequência de Fibonacci

n = int(input('\nDigite um número inteiro: '))
c = 0
i = n + 1
print(n, end=' -> ')
while c != 7:
    seq = n + i
    print(seq, end=' -> ')
    n = seq
    c += 1
    
    