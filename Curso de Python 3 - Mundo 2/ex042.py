#Complemento do exercise 35 - Triângulos

r1 = float(input('\nComprimento do primeiro segmento: '))
r2 = float(input('Comprimento do segundo segmento: '))
r3 = float(input('Comprimento do terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f"\n\033[4;32mOs segmentos podem formar um triângulo!\033[m\n")
else:
    print(f"\n\033[4;31mOs segmento Não podem formar um triângulo!\033[m\n")
    
if r1 == r1 and r1 == r3 and r2 == r3:
    print(f"É um triângulo equilátero.\n")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print(f"É um triângulo isósceles.\n")
else:
    print("É um triângulo escaleno.\n")
