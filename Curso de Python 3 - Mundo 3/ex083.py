#Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses. O aplicativo irá analizar e dizer se os parênteses estão abertos e fechado na ordem correta.

lista = []
p1 = p2 = soma = 0
error = 1
exp = lista.append(str(input('Digite uma expressão: ')))

for c in lista:
    for i in c:
        if i in '(':
            p1 += 1
        elif i in ')':
            p2 += 1
        if p2 > p1:
            error = 0
    soma = p1 + p2
    
    if soma%2 != 0 or error == 0:
        print("Sua expressão está errada!")
    else:
        print("Sua expressão está válida!")
