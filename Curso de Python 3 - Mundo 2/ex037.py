#Digite um número e escolha se quer converte-lo para binário, octal ou hexadecimal

num = int(input('\nDigite um número: '))
e = int(input('\n\033[1;37mConversão - Digite:\n1 para binário \n2 para octal \n3 hexadecimal\033[m \n\n'))

if e == 1:
    print(f"\nO número {num} em binário é : \033[4;32m{bin(num)}\033[m\n")
    
elif e == 2:
    print(f"\nO número {num} em octal é: \033[4;32m{oct(num)}\033[m\n")
    
elif e == 3:
    print(f"\nO número {num} em hexadecimal é: \033[4;32m{hex(num)}\033[m\n")
