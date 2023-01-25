#Leia um  número qualquer e mostre seu fatorial

num = int(input('\nDigite um número para ver qual o seu fatorial: '))

c = num
x = (num)
resultado = 1

while c != 1:
    c += -1
    j = str(c)
    resultado = num*c
    num = resultado
print(f"\n{x}! = {resultado}\n")
