#Leia dois valores inteirose compare mostrando qual é o maior ou se são iguais.

v1 = int(input('\nInsira um valor inteiro: '))
v2 = int(input('Insira outro valor inteiro: '))

if v1 > v2:
    print(f"\nO primeiro valor é o maior!\n")
elif v2 > v1:
    print(f"\nO segundo valor é o maior!\n")
else:
    print(f"\nNão existe maior valor, os dois são iguais.\n")