#Tabuada de um nº inteiro

n = int(input('\n\033[1;32mDigite um número inteiro: \033[m'))
x = 1
print('')
for c in range(1,11):
    print(f"{n} x {c} = {n*c}")
print()