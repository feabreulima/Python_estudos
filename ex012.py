#Preço de um produto qualquer com de descontos e com juros


print('==============================================================')

product = float(input('Digite o preço do produto: R$ '))

price1 = product * 0.95

price2 = product * 0.90

price3 = price1 * 0.90

price4 = product * 1.08

print(f'\nO novo preço do produto com 5% de desconto é: R$ {price1:.2f}\n')
print(f'O preço do produto caso seje pago a vista (10% de desconto): R$ {price2:.2f} \nPreço com desconto e avista (15% de desconto): R$ {price3:.2f}\n')

parcela = int(input('Digite quantas parcelas você quer pagar: '))
price5 = (price4/parcela)
print(f'O preço total do produto caso seja parcelado (+8%): R$ {price4:.2f} \nPreço por cada parcela: R$ {price5:.2f}')

print('==============================================================')

