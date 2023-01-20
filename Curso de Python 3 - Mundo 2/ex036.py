#Leia o valor de uma casa, o salário do comprador e o número de anos que ele irá pagar.Calcula se a prestação não irá exceder 30% do salário.

valorCasa = float(input('\nQual o valor da casa? R$ '))
salario = float(input('Qual seu salário? R$ '))
anos = 12 * float(input('Em quantos anos quer pagar? '))

prestacao = (valorCasa / anos)
minimo = salario*0.30

if prestacao > minimo:
    print(f"\nAs parcelas comprometem mais de 30% do seu salário. Empréstimo negado...\n")
else:
    print(f"\nEmpréstimo aprovado!\n")
