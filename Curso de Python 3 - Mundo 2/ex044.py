#Leia o preço de um produto a ser pago e mostre o descontos ou juros de acordo com a condição de pagamento

produto = float(input('\nQual o preço do produto? R$ '))
digito = int(input("\nQual a forma de pagamento? \n\nDigite:\n1 - Para à vista no dinheiro/cheque (10% de desconto)\n2 - Para à vista no cartão (5% de desconto)\n3 - Para 2x no cartão (preço normal)\n4 - Para 3x ou mais no cartão (20% de *juros*)\n\n"))

if digito == 1:
    print(f"\nO valor à vista sai a R$ {produto*0.90:.2f}\n")
elif digito == 2:
    print(f"\nO valor à vista sai a R$ {produto*0.95:.2f}\n")
elif digito == 3:
    print(f"\nO valor sai a duas parcelas de R$ {produto/2:.2f}\n")
elif digito == 4:
    parcelas = int(input('\nAcima de 2 parcelas, quantas vezes quer parcelar? '))
    print(f"\nO valor sai a R$ {produto*1.20/parcelas} cada parcela.\n")
