#Leia o salário de um funcionário e calcule seu aumento, se salário for menor/igual que R$ 1.250,00 , 15% de aumento, caso salário acima, 10% de aumento

salario = float(input('\nInforme seu salário: R$ '))

if salario <= 1250:
    aumento = salario*0.15
    print(f'\nSeu aumento é de (+15%): R$ {aumento:.2f}\nSeu salário agora são R$ {aumento+salario:.2f}\n')
else:
    aumento = salario*0.10
    print(f'\nSeu aumento é de (+10%): R$ {aumento:.2f}\nSeu salário agora são R$ {aumento+salario:.2f}\n')