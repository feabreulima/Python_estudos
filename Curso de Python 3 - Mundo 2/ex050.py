#Leia seis números e mostre a soma apenas dos pares

soma = 0
print('')
for c in range(1,7):
    x = int(input('Digite um número inteiro: '))
    if x %2 ==0:
        soma += x
print('')
print(f"A soma dos números pares são {soma}\n")
