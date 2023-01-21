#Leia o peso de 5 pessoas e mostre o ma

pesos = []

for c in range(1,6):
    pesos.append(float(input('\nInsira o peso da pessoa em Kg: ')))
x = sorted(pesos)

print(f"\nO maior peso é {x[-1]} Kg e o menor peso é {x[0]} Kg\n")
